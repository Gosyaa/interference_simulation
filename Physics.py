def OPD (x, d, L):
    return (d * (x / L))

def wavelength_to_rgb(wavelength):
    gamma = 0.8
    if 380 <= wavelength < 440:
        r =(440 - wavelength) / (440 - 380)
        g = 0.0
        b = 1.0
    elif 440 <= wavelength < 490:
        r = 0.0
        g = (wavelength - 440) / (490 - 440)
        b = 1.0
    elif 490 <= wavelength < 510:
        r = 0.0
        g = 1.0
        b = (510 - wavelength) / (510 - 490)
    elif 510 <= wavelength < 580:
        r = (wavelength - 510) / (580 - 510)
        g = 1.0
        b = 0.0
    elif 580 <= wavelength < 645:
        r = 1.0
        g = (645 - wavelength) / (645 - 580)
        b = 0.0
    elif 645 <= wavelength < 781:
        r = 1.0 
        g = 0.0
        b = 0.0
    else:
        r = 0.0
        g = 0.0
        b = 0.0

    factor = 0.0
    if 380 <= wavelength < 420:
        factor = 0.3 + 0.7 * (wavelength - 380) / (420 - 380)
    elif 420 <= wavelength < 701:
        factor = 1.0
    elif 701 <= wavelength < 781:
        factor = 0.3 + 0.7 * (780 - wavelength) / (780 - 700)

    r = (r * factor)**gamma
    g = (g * factor)**gamma
    b = (b * factor)**gamma
    return (r, g, b)

def fix_hex (s):
    if len(s) == 1:
        return '0' + s
    return s

def rgb_to_hex(rgb, max_intensity = 1.0):
    tmp = 255 * max_intensity
    r_res = fix_hex(hex(int(rgb[0] * tmp))[2:])
    g_res = fix_hex(hex(int(rgb[1] * tmp))[2:])
    b_res = fix_hex(hex(int(rgb[2] * tmp))[2:])

    res = r_res + g_res + b_res
    return ('#' + res)
