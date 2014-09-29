from bs4 import BeautifulSoup
from models import *
from forms import *
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory



def compute_packet_requirements(qset):
    '''
    :param qset: a QuestionSet model object
    :return: a collection of SetWideDistributionEntry objects
    '''

    num_packets = qset.num_packets
    packets = qset.packet_set.all()
    dist = qset.distribution
    dist_entries = dist.distributionentry_set.all()

    set_wide_entries = []

    for dist_entry in dist_entries:
        req_tus = dist_entry.min_tossups
        req_bs = dist_entry.min_bonuses

        set_wide_entry = SetWideDistributionEntry()
        set_wide_entry.category = dist_entry.category
        set_wide_entry.subcategory = dist_entry.subcategory
        set_wide_entry.num_tossups = req_tus
        set_wide_entry.num_bonuses = req_bs

        set_wide_entries.append(set_wide_entry)

    return set_wide_entries

def create_set_distro_formset(qset):

    DistributionEntryFormset = formset_factory(SetWideDistributionEntryForm, can_delete=False, extra=0)
    entries = qset.setwidedistributionentry_set.all()
    initial_data = []
    for entry in entries:
        initial_data.append({'entry_id': entry.id,
        'dist_entry': entry.dist_entry,
        'category': entry.dist_entry.category,
        'subcategory': entry.dist_entry.subcategory,
        'num_tossups': entry.num_tossups,
        'num_bonuses': entry.num_bonuses})
    return DistributionEntryFormset(initial=initial_data, prefix='distentry')

def get_role(user, qset):

    role = 'viewer'
    qset_editors = qset.editor.all()
    qset_writers = qset.writer.all()

    if user in qset_editors and user != qset.owner:
        role = 'editor'
    elif user in qset_writers:
        role = 'writer'
    elif user == qset.owner:
        role = 'owner'

    return role
