import glob
import json
import hashlib
import datetime
import re

from discorddump.model import sm, Event

db = sm()
seen_event_hashs = set(_[0] for _ in db.query(Event.event_hash))
seen_event_types = set()
to_commit = []

def do_commit():
    db.bulk_insert_mappings(
        Event,
        to_commit,
    )
    db.commit()
    print(f"Commited {len(to_commit)} to DB.", flush=True)
    to_commit.clear()

def get_date(timestamp):
    if isinstance(timestamp, int):
        return datetime.datetime.utcfromtimestamp(blob["timestamp"] / 1000)

    if isinstance(timestamp, str):
        return datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
    
    raise Exception(f"WTF IS THIS TIMESTAMP {timestamp}")

for filename in glob.glob("package/activity/**/*.json", recursive=True):
    file_source = re.search(r"activity/(\w+)/", filename).group(1)

    with open(filename, "r") as f:
        for line in f:
            blob = json.loads(line)
            blob_hash = hashlib.md5(line.encode("utf8")).hexdigest()

            if blob_hash not in seen_event_hashs:
                seen_event_hashs.add(blob_hash)
            else:
                # print(f"Event {blob['event_id']} has been seen before. [{blob_hash}]")
                continue

            if blob["event_type"] not in seen_event_types:
                seen_event_types.add(blob["event_type"])
                print(f"New event type: {blob['event_type']}.")

            to_commit.append(dict(
                event_id=blob["event_id"],
                event_hash=blob_hash,
                event_type=blob["event_type"],
                event_source=file_source,
                timestamp=get_date(blob["timestamp"]),
                blob=blob,
            ))
            
            if len(to_commit) > 1024:
                do_commit()

do_commit()