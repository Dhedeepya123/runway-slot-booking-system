from datetime import datetime


def has_conflict(existing_start, existing_end, new_start, new_end):
    """
    Returns True if two time slots overlap
    """

    existing_start = datetime.strptime(existing_start, "%H:%M")
    existing_end = datetime.strptime(existing_end, "%H:%M")
    new_start = datetime.strptime(new_start, "%H:%M")
    new_end = datetime.strptime(new_end, "%H:%M")

    # Overlap condition
    return not (new_end <= existing_start or new_start >= existing_end)


def find_next_available_slot(bookings, start_time, end_time):
    """
    Suggest next available slot if conflict occurs
    """

    base_start = datetime.strptime(start_time, "%H:%M")
    base_end = datetime.strptime(end_time, "%H:%M")

    duration = base_end - base_start

    current_start = base_start

    while True:
        conflict = False

        for b in bookings:
            if has_conflict(b.start_time, b.end_time,
                            current_start.strftime("%H:%M"),
                            (current_start + duration).strftime("%H:%M")):
                conflict = True
                break

        if not conflict:
            return current_start.strftime("%H:%M"), (current_start + duration).strftime("%H:%M")

        current_start = current_start + duration