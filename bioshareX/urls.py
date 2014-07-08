from django.conf.urls import patterns, include, url
from bioshareX.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import urls

urlpatterns = patterns('bioshareX.views',
    url(r'^/?$', 'index', name='index'),
    url(r'^forbidden/?$', 'forbidden', name='forbidden'),
    url(r'^create/?$', 'create_share', name='create_share'),
    url(r'^edit/(?P<share>\w{15})/?$', 'edit_share', name='edit_share'),
    url(r'^cloud/?$', 'tag_cloud', name='tag_cloud'),
#     url(r'^list/(?P<share>\w{15})/$', 'list_directory', name='list_directory'),
#     url(r'^list/(?P<share>\w{15})/(?P<subdir>.*/)$', 'list_directory', name='list_sub_directory'),
    url(r'^list/(?P<share>[\da-zA-Z]{15})/(?:(?P<subdir>.*/))?$', 'list_directory', name='list_directory_old'),
    url(r'^view/(?P<share>[\da-zA-Z]{15})/(?:(?P<subdir>.*/))?$', 'list_directory', name='list_directory'),
    url(r'^wget/(?P<share>[\da-zA-Z]{15})/(?:(?P<subdir>.*/))?wget_index.html$', 'wget_listing', name='wget_listing'),
    url(r'^shares/?$', 'list_shares', name='list_shares'),
    url(r'^permissions/(?P<share>[\da-zA-Z]{15})/?$', 'share_permissions', name='share_permissions'),
    url(r'^goto/(?P<share>[\da-zA-Z]{15})/(?:(?P<subpath>.*/?))?$', 'go_to_file_or_folder', name='go_to_file_or_folder'),
    url(r'^ssh_keys/list/?$', 'list_ssh_keys', name='list_ssh_keys'),
    url(r'^ssh_keys/create/?$', 'create_ssh_key', name='create_ssh_key'),
#     url(r'^account/update_password/?$', 'update_password', name='update_password'),
    url(r'^delete_share/(?P<share>[\da-zA-Z]{15})/?$', 'delete_share', kwargs={'confirm':False},name='delete_share'),
    url(r'^confirm_delete_share/(?P<share>[\da-zA-Z]{15})/?$', 'delete_share', kwargs={'confirm':True},name='confirm_delete_share'),
    url(r'^search/files/?$', 'search_files', name='search_files'),
)

urlpatterns += patterns('',
    url(r'^account/update_password/$', 'django.contrib.auth.views.password_change',  {'password_change_form': PasswordChangeForm},name='update_password'),
)

urlpatterns += patterns('bioshareX.api',
    url(r'^api/get_permissions/(?P<share>[\da-zA-Z]{15})/?$', 'get_permissions', name='api_get_permissions'),
    url(r'^api/get_user_permissions/(?P<share>[\da-zA-Z]{15})/?$', 'get_user_permissions', name='api_get_user_permissions'),
    url(r'^api/share_metadata/(?P<share>[\da-zA-Z]{15})/?$', 'get_share_metadata', name='api_get_share_metadata'),
    url(r'^api/set_permissions/(?P<share>[\da-zA-Z]{15})/?$', 'set_permissions', name='api_set_permissions'),
    url(r'^api/update/(?P<share>[\da-zA-Z]{15})/?$', 'update_share', name='api_update_share'),
    url(r'^api/share_with_emails/?$', 'share_with_emails', name='api_share_with_emails'),
    url(r'^api/get_group/?$', 'get_group', name='api_get_group'),
    url(r'^api/search/(?P<share>[\da-zA-Z]{15})/(?:(?P<subdir>.*/))?$', 'search_share', name='api_search_share'),
    url(r'^api/share_autocomplete/$', 'share_autocomplete', name='api_share_autocomplete'),
    url(r'^api/ssh_keys/delete/?$', 'delete_ssh_key', name='api_delete_ssh_key'),
    url(r'^api/edit_metadata/(?P<share>[\da-zA-Z]{15})/(?P<subpath>.*)/?$', 'edit_metadata', name='api_edit_metadata'),
    url(r'^api/get_addresses/?$', 'get_address_book', name='api_get_address_book'),
)

urlpatterns += patterns('bioshareX.file_views',
#     url(r'^upload/(?P<share>\w{15})(?:/?P<subdir>.*/)$', 'upload_file', name='upload_file'),
#     url(r'^upload/?$', 'upload_file', name='upload_file'),
    url(r'^upload/(?P<share>[\da-zA-Z]{15})/(?:(?P<subdir>.*/))?$', 'upload_file', name='upload_file'),
    url(r'^create_folder/(?P<share>[\da-zA-Z]{15})/(?:(?P<subdir>.*/))?$', 'create_folder', name='create_folder'),
    url(r'^rename/(?P<share>[\da-zA-Z]{15})/(?:(?P<subdir>.*/))?$', 'modify_name', name='modify_name'),
    url(r'^delete/(?P<share>[\da-zA-Z]{15})/(?:(?P<subdir>.*/))?$', 'delete_paths', name='delete_paths'),
    url(r'^move/(?P<share>[\da-zA-Z]{15})/(?:(?P<subdir>.*/))?$', 'move_paths', name='move_paths'),
    url(r'^archive/(?P<share>[\da-zA-Z]{15})/(?:(?P<subdir>.*/))?$', 'archive_files', name='archive_files'),
    url(r'^download/(?P<share>[\da-zA-Z]{15})/(?P<subpath>.*)/?$', 'download_file', name='download_file'),
    url(r'^download_archive/(?P<share>[\da-zA-Z]{15})/(?P<subpath>.*)/?$', 'download_archive', name='download_archive'),
    url(r'^preview/(?P<share>[\da-zA-Z]{15})/(?P<subpath>.*)/?$', 'preview_file', name='preview_file'),
    url(r'^directories/(?P<share>[\da-zA-Z]{15})/?$', 'get_directories', name='get_directories'),
    url(r'^wget/(?P<share>[\da-zA-Z]{15})/(?P<subpath>.*)/?$', 'download_file', name='wget_download_file'),
)
