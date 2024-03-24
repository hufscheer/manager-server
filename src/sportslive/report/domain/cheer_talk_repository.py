from report.domain import CheerTalk
from django.shortcuts import get_object_or_404

class CheerTalkRepository:
    def find_is_blocked_cheer_talks(self):
        return CheerTalk.objects.order_by('-created_at').filter(is_blocked=True)
    
    def find_cheer_talk_by_id(self, cheer_talk_id: int):
        return get_object_or_404(CheerTalk, id=cheer_talk_id)
    
    def save_cheer_talk(self, cheer_talk: CheerTalk):
        cheer_talk.save()