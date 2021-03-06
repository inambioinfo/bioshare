from bioshareX.models import ShareLog, Share, Tag, ShareStats, Message
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from guardian.shortcuts import get_users_with_perms, get_groups_with_perms
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','username')
    def __init__(self, *args, **kwargs):
        self.include_perms = kwargs.pop('include_perms', False)
        super(UserSerializer,self).__init__(*args,**kwargs)
    def to_representation(self, instance):
        data = serializers.ModelSerializer.to_representation(self, instance)
        if self.include_perms:
            data['permissions'] = instance.get_all_permissions()
            groups = Group.objects.all() if instance.is_superuser else instance.groups.all()
            data['groups'] = [{'id':g.id,'name':g.name,'permissions':instance.get_all_permissions(g)} for g in groups]
        return data

class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(source='user_set',many=True, read_only=True)
    class Meta:
        model = Group
        fields = ('id','name','users')
    def to_representation(self, instance):
        data = serializers.ModelSerializer.to_representation(self, instance)
        user_perms = get_users_with_perms(instance,attach_perms=True,with_group_users=False)
#         data['permissions'] = [{'user':UserSerializer(user).data,'permissions':permissions} for user, permissions in user_perms.iteritems()]
        perm_map = {user.id:permissions for user, permissions in user_perms.iteritems()}
        for user in data['users']:
            user['permissions'] = [] if not perm_map.has_key(user['id']) else perm_map[user['id']]
        return data
class ShareLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    paths = serializers.JSONField()
    class Meta:
        model = ShareLog

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag

class ShareStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareStats
        fields = ('num_files','bytes','updated')

class ShareSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    users = serializers.SerializerMethodField(read_only=True)
    groups = serializers.SerializerMethodField(read_only=True)
    stats = ShareStatsSerializer(many=False,read_only=True)
    tags = TagSerializer(many=True,read_only=True)
    owner = UserSerializer(read_only=True)
    def get_url(self,obj):
        return obj.get_url()
    def get_users(self,obj):
        return list(set([p.user.username for p in obj.user_permissions.all()]))
#         return [u.email for u in get_users_with_perms(obj,attach_perms=False,with_group_users=False)]
    def get_groups(self,obj):
        return list(set([p.group.name for p in obj.group_permissions.all()]))
#         return [g.name for g in get_groups_with_perms(obj,attach_perms=False)]
    class Meta:
        model = Share
        fields = ('id','url','users','groups','stats','tags','owner','slug','created','updated','name','secure','read_only','notes','path_exists')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id','created','title','description')
