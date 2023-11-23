import badger2040
import badger_os

MARQUEE_START_X_POSN = -210
MARQUEE_ORIG_X_POSN = 44
is_warning_displayed = False

badger = badger2040.Badger2040()

def write_original_text():
    badger.set_update_speed(badger2040.UPDATE_MEDIUM)

    badger.set_pen(15)
    badger.clear()

    badger.set_pen(0)
    badger.set_font("bitmap8")
    badger.text("Harsh", 35, 5, scale=9)
    badger.text("Kapadia", MARQUEE_ORIG_X_POSN, 78, scale=6)
    badger.update()

# Move text from left to right in a loop
def marquee_text():
    global is_warning_displayed
    i = MARQUEE_ORIG_X_POSN

    if is_warning_displayed:
        is_warning_displayed = False
        write_original_text()

    badger.set_update_speed(badger2040.UPDATE_TURBO)

    while True:
        i = i + 10

        badger.set_pen(15)
        badger.clear()

        badger.set_pen(0)
        badger.set_font("bitmap8")
        badger.text("Kapadia", i, 78, scale=6)
        badger.partial_update(0, 72, badger2040.WIDTH, badger2040.HEIGHT - 72)

        if i >= badger2040.WIDTH:
            i = MARQUEE_START_X_POSN
        if badger.pressed(badger2040.BUTTON_C):
            write_original_text()
            break
        if badger.pressed(badger2040.BUTTON_B):
            is_warning_displayed = True
            badger.set_update_speed(badger2040.UPDATE_MEDIUM)
            badger_os.warning(badger, "Press 'A' to start looping text from left to right. Press 'C' to stop.")
            break

def main():
    global is_warning_displayed

    write_original_text()

    while True:
        # Sometimes a button press or hold will keep the system
        # powered *through* HALT, so latch the power back on.
        badger.keepalive()

        if badger.pressed(badger2040.BUTTON_A):
            marquee_text()
        if badger.pressed(badger2040.BUTTON_B):
            if not is_warning_displayed:
                is_warning_displayed = True
                badger_os.warning(badger, "Press 'A' to start looping text from left to right. Press 'C' to stop.")
            else:
                is_warning_displayed = False
                write_original_text()

        # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
        badger.halt()

main()
