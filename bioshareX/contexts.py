from models import Share
from guardian.shortcuts import get_objects_for_user
from django.conf import settings
def user_contexts(request):
        if request.user.is_authenticated() and not request.is_ajax():
            recent_shares = Share.objects.filter(owner=request.user).order_by('-created')[:5]
            shared_with_me = get_objects_for_user(request.user, 'bioshareX.view_share_files',klass=Share).exclude(owner=request.user).order_by('-created')[:5]
            bad_share_path = get_objects_for_user(request.user, 'bioshareX.view_share_files',klass=Share).filter(path_exists=False).order_by('-created')
        else:
            recent_shares = []
            shared_with_me = []
            bad_share_path = [] 
        return {
            'my_recent_shares':recent_shares,
            'shared_with_me':shared_with_me,
            'bad_share_path':bad_share_path,
            'SITE_URL':settings.SITE_URL
        }



# def user_dashboard(request, template_name='projects/dashboard.html'):
#     projects = get_objects_for_user(request.user, 'projects.view_project')
#     return render_to_response(template_name, {'projects': projects},
#         RequestContext(request))