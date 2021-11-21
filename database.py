import redis
import pickle
import os
from hashlib import blake2b


class DataBase:

    def __init__(self, host, port):
        self.db = redis.Redis(
            port=port,
            host=host
        )
        self.list_of_keys = 'list_of_keys'

    def add_task_to_db(self, task, key=None):
        packed_task = pickle.dumps(task)
        if not key:
            hashed_title = blake2b(salt=os.urandom(blake2b.SALT_SIZE))
            hashed_title.update(packed_task)
            key = hashed_title.hexdigest()
            self.db.rpush(self.list_of_keys, key)

        self.db.set(key, packed_task)

    def _get_task_from_db(self, key):
        return pickle.loads(self.db.get(key))

    def _remove_task_from_db(self, key):
        self.db.delete(key)
        self.db.lrem(self.list_of_keys, count=1, value=key)

    def _get_tasks_keys(self):
        return self.db.lrange(self.list_of_keys, 0, -1)

    def get_all_tasks(self):
        keys = self._get_tasks_keys()
        tasks_dict = {}
        if keys:
            for idx, key in enumerate(keys):
                tasks_dict[idx] = self._get_task_from_db(key=key)

        return tasks_dict

    def remove_task_by_idx(self, idx):
        keys = self._get_tasks_keys()
        self._remove_task_from_db(key=keys[idx])

    def modify_task_by_idx(self, task_id):
        keys = self._get_tasks_keys()
        task = self._get_task_from_db(keys[task_id])
        task.change_completion()
        self.add_task_to_db(task, keys[task_id])
