# room_detector.py


def f(detector):
    current_people = 0
    max_people = 0

    for event in detector:
        if event == "+":
            current_people += 1
        elif event == "-":
            current_people -= 1

        if current_people > max_people:
            max_people = current_people

    return max_people >= 3
