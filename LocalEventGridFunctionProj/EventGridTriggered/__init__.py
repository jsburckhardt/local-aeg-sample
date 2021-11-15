import json
import logging

import azure.functions as func


def main(event: func.EventGridEvent):
    try:
        logging.info(f"ID: {event.id}")
        logging.info(f"DATA_MESSAGE: {event.get_json()['message']}")
        result = json.dumps(
            {
                "id": event.id,
                "data": event.get_json(),
                "topic": event.topic,
                "subject": event.subject,
                "event_type": event.event_type,
            }
        )
    except Exception as e:
        logging.error(e)

    logging.info("Python EventGrid trigger processed an event: %s", result)
