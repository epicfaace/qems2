from django.conf.urls import include, url
from django.contrib.auth.views import logout, login, password_change, password_change_done
from django.views.generic import ListView
from qems2.qsub.views import *
from qems2.qsub.models import *

import django

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'QuEST.views.home', name='home'),
    # url(r'^QuEST/', include('QuEST.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', admin.site.urls),
    
    # accounts
    url(r'^accounts/', include('allauth.urls')),
    
    url(r'^main/$', main),
    url(r'^$', main),
    url(r'^profile/$', profile),    
    
    url(r'^question_sets/$', question_sets),
    url(r'^create_question_set/$', create_question_set),
    url(r'^edit_question_set/(?P<qset_id>[0-9]+)/$', edit_question_set),
    url(r'^distributions/$', distributions),
    url(r'^add_editor/(?P<qset_id>[0-9]+)/$', add_editor),
    url(r'^add_writer/(?P<qset_id>[0-9]+)/$', add_writer),
    url(r'^edit_distribution/(?P<dist_id>[0-9]+)/$', edit_distribution),
    url(r'^edit_distribution/$', edit_distribution),
    url(r'^edit_tiebreak/(?P<dist_id>[0-9]+)/$', edit_tiebreak),
    url(r'^edit_tiebreak/$', edit_tiebreak),
    url(r'^edit_set_distribution/(?P<qset_id>[0-9]+)/$', edit_set_distribution),
    url(r'^edit_set_tiebreak/(?P<qset_id>[0-9]+)/$', edit_set_tiebreak),
    url(r'^add_tossups/(?P<qset_id>[0-9]+)/$', add_tossups),
    url(r'^add_tossups/(?P<qset_id>[0-9]+)/(?P<packet_id>[0-9]+)/$', add_tossups),
    url(r'^edit_tossup/(?P<tossup_id>[0-9]+)/$', edit_tossup),
    url(r'^delete_tossup/$', delete_tossup),
    url(r'^add_bonuses/(?P<qset_id>[0-9]+)/(?P<bonus_type>.+)/$', add_bonuses),
    url(r'^add_bonuses/(?P<qset_id>[0-9]+)/(?P<bonus_type>.+)/(?P<packet_id>[0-9]+)/$', add_bonuses),
    url(r'^edit_bonus/(?P<bonus_id>[0-9]+)/$', edit_bonus),
    url(r'^delete_bonus/$', delete_bonus),
    url(r'^add_packets/(?P<qset_id>[0-9]+)/$', add_packets),
    url(r'^edit_packet/(?P<packet_id>[0-9]+)/$', edit_packet),
    url(r'^type_questions/$', type_questions),
    url(r'^type_questions/(?P<qset_id>[0-9]+)/$', type_questions),
    url(r'^type_questions_edit/(?P<question_type>.+)/(?P<question_id>[0-9]+)/$', type_questions_edit),    
    #url(r'^edit_packet/(?P<packet_id>[0-9]+)/change_tossup_position/(?P<old_index>[0-9]+)/(?P<new_index>[0-9]+)$', change_tossup_order),
    #url(r'^edit_packet/(?P<packet_id>[0-9]+)/change_bonus_position/(?P<old_index>[0-9]+)/(?P<new_index>[0-9]+)$', change_bonus_order),
    url(r'^delete_packet/$', delete_packet),
    url(r'^settings/$', settings),
    url(r'^logout/$', logout_view),   
    url(r'^categories/(?P<qset_id>[0-9]+)/(?P<category_id>[0-9]+)/$', categories),
    url(r'^export_question_set/(?P<qset_id>[0-9]+)/(?P<output_format>.+)/$', export_question_set),
    url(r'^delete_writer/$', delete_writer),
    url(r'^delete_editor/$', delete_editor),
    url(r'^delete_set/$', delete_set),    
    url(r'^delete_comment/$', delete_comment),
    url(r'^restore_tossup/$', restore_tossup),
    url(r'^restore_bonus/$', restore_bonus),
    url(r'^tossup_history/(?P<tossup_id>[0-9]+)/$', tossup_history),
    url(r'^bonus_history/(?P<bonus_id>[0-9]+)/$', bonus_history),
    url(r'^questions_remaining/(?P<qset_id>[0-9]+)/$', questions_remaining),
    url(r'^bulk_change_set/(?P<qset_id>[0-9]+)/$', bulk_change_set),
    url(r'^writer_question_set_settings/(?P<qset_id>[0-9]+)/$', writer_question_set_settings),    
    url(r'^contributor/(?P<qset_id>[0-9]+)/(?P<writer_id>[0-9]+)/$', contributor),
              
    url(r'^upload_questions/(?P<qset_id>[0-9]+)/$', upload_questions),
    url(r'^complete_upload/$', complete_upload),
    url(r'^move_tossup/(?P<q_set_id>[0-9]+)/(?P<tossup_id>[0-9]+)/$', move_tossup),
    url(r'^move_bonus/(?P<q_set_id>[0-9]+)/(?P<bonus_id>[0-9]+)/$', move_bonus),
    url(r'^convert_tossup/$', convert_tossup),
    url(r'^convert_bonus/$',convert_bonus),
    url(r'^view_all_questions/(?P<qset_id>[0-9]+)/$',view_all_questions),    
    url(r'^view_all_comments/(?P<qset_id>[0-9]+)/$',view_all_comments),    
    url(r'^question_set_distribution/(?P<qset_id>[0-9]+)/$',question_set_distribution),    
    
    # json calls
    url(r'^get_unassigned_tossups/$', get_unassigned_tossups),
    url(r'^get_unassigned_bonuses/$', get_unassigned_bonuses),
    url(r'^assign_tossups_to_packet/$', assign_tossups_to_packet),
    url(r'^assign_bonuses_to_packet/$', assign_bonuses_to_packet),
    url(r'^change_question_order/$', change_question_order),
    #url(r'^change_tossup_position/$', change_tossup_order),
    #url(r'^change_bonus_position/$', change_bonus_order),

    # commenting framework
    url(r'^comments/', include('django_comments.urls')),

    # search
    # url(r'^search/', include('haystack.urls')),
    url(r'^search/$', search),
    url(r'^search/(?P<passed_qset_id>[0-9]+)/$', search),
    
    #auth
    #url(r'^accounts/', include('allauth.urls')),
]

#import debug_toolbar
#urlpatterns += patterns('',
#    url(r'^__debug__/', include(debug_toolbar.urls)),
#)
