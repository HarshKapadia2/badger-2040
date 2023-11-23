# Badger 2040

My experimentation with the [Badger 2040](https://shop.pimoroni.com/products/badger-2040) hardware that I got at [GitHub Universe](https://githubuniverse.com) 2023.

Context and details: https://github.com/badger2040/home

## Examples

### Marquee Name

https://github.com/HarshKapadia2/badger-2040/assets/50140864/aa9a8f42-4cdd-436f-9213-995064bbd292

-   Loops text from left to right like [the HTML Marquee tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/marquee).
-   Buttons
    -   `A`: Start looping
    -   `C`: Stop looping
    -   `B`: Display instructions
-   Files: [`examples/mname.py`](examples/mname.py) and [`examples/icon-mname.jpg`](examples/icon-mname.jpg)

### Profiles

https://github.com/HarshKapadia2/badger-2040/assets/50140864/e32dbfbb-4af7-494b-99e5-6517c62fba59

-   Loops through user profiles in [`/profiles`](profiles).
-   Buttons
    -   `UP` and `DOWN`: Loop through the profile files in [`/profiles`](profiles)
    -   `B`: Display instructions
-   Files
    -   [`examples/profiles.py`](examples/profiles.py) and [`examples/icon-profiles.jpg`](examples/icon-profiles.jpg)
    -   Profiles
        -   Profile data (`.txt` only) and logos (`.jpg` only) should be placed in [`/profiles`](profiles).
        -   Profile data format (Place the following on one line each.)
            -   `uri`: Path to logo starting with `/profiles/...`
            -   `is_qr_code`: Is the `uri` to be rendered as a QR code? (Not implemented yet, so value does not matter.)
            -   `uri_x`: Logo/QR Code position from the left of the screen
            -   `uri_y`: Logo/QR Code position from the top of the screen
            -   `name`: Name to be displayed
            -   `name_x`: Name position from the left of the screen
            -   `name_scale`: Scale/size of the text (Value range: 0 to 1)
            -   `post`: Position in an organisation
            -   `post_x`: Post position from the left of the screen
            -   `org`: Name of the organisation
            -   `org_x`: Organisation name position from the left of the screen
            -   `pronouns`: User's pronouns
            -   `pronouns_x`: User's pronoun position from the left of the screen
        -   Sample profiles
            -   AMD: [`profiles/amd.txt`](profiles/amd.txt) and [`profiles/amd-logo.jpg`](profiles/amd-logo.jpg)
            -   OTC: [`profiles/otc.txt`](profiles/otc.txt) and [`profiles/otc-logo.jpg`](profiles/otc-logo.jpg)

## Resources

-   [Get started (with some context)](https://github.com/badger2040/home)
-   [Getting Started with Badger 2040](https://learn.pimoroni.com/article/getting-started-with-badger-2040)
-   [Badger 2040 function reference](https://github.com/pimoroni/badger2040/blob/main/docs/reference.md)
-   [Text, image and other graphics](https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/modules/picographics/README.md)
-   [`badger_os` module](https://github.com/pimoroni/badger2040/blob/main/firmware/PIMORONI_BADGER2040/lib/badger_os.py)
-   [Badger 2040 official repository](https://github.com/pimoroni/badger2040)
-   [GitHub's Badger 2040 repository](https://github.com/badger2040/badgerbodger)
-   [Badger 2040 Schedule](https://github.com/creativenucleus/badger-2040-schedule)
-   [Raspberry Pi Pico](https://raspberrytips.com/what-is-raspberry-pi-pico)
