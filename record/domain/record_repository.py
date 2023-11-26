from record.domain import Record

class RecordRepository:
    def save_record(self, record: Record):
        record.save()