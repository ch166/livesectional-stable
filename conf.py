# -*- coding: utf-8 -*- #
"""
Created on Oct 28 - 2021.

@author: chris.higgins@alternoc.net
"""

import re
import configparser

# This configuration parser provides access to the key/value data stored in
# the config.ini file. It currently uses configparser as the backend for managing ini files.
# .ini files are useful for swapping data with humans
# Future work in this space should look at storing the config as either
# - json - structured, able to store more data cleanly
#        - harder to handle random external generated configs through the export/import process
# - toml - more rigid .ini file equivalent
#
# What would be really useful ;
#   - a config file format that supports persistance of comments across load - parse - save cycles.
#   - a config file format that allows file imports
#
# There are snippets of the configuration that are site hardware implementation specific, and
# snippets of the configuration that are 'end user' airport / settings specific. It would be useful
# to be able to swap out / reset the 'end user' pieces of the configuration without losing the
# configuration state for the hardware (LED , OLED , Switch setup )


class Conf:
    """Configuration Class."""

    def __init__(self):
        """Initialize and load configuration."""
        self.config_filename = "config.ini"
        self.configfile = configparser.ConfigParser()
        self.configfile._interpolation = configparser.ExtendedInterpolation()
        self.configfile.read(self.config_filename)

    def get(self, section, key):
        """Read Setting."""
        return self.configfile.get(section, key)

    def color(self, section, key):
        """Pull out color value in hex."""
        return self.configfile.get(section, key)

    def get_color_decimal(self, section, key):
        """Read three tuple string, Return as tuple of integers."""
        color_list = []
        tmp_string = self.configfile.get(section, key)
        # print("tmp_string:" + tmp_string + ":--")
        # color_list = tmp_string.split(',')
        color_list = re.split(r"[(),\s]\s*", tmp_string)
        # print(type(color_list))
        # print(len(color_list))
        # print("-=-=-=-=-=-=-")
        # print(color_list)
        # print("-=-=-=-=-=-=-")
        rgb_r = int(color_list[0])
        rgb_g = int(color_list[1])
        rgb_b = int(color_list[2])
        # print(rgb_r, rgb_g, rgb_b)
        # print("-=-=-=-=-=-=-")

        return tuple([rgb_r, rgb_g, rgb_b])

    def get_string(self, section, key):
        """Read Setting."""
        return self.configfile.get(section, key)

    def set_string(self, section, key, value):
        """Set String Value."""
        self.configfile.set(section, key, value)

    def get_bool(self, section, key):
        """Read Setting."""
        return self.configfile.getboolean(section, key)

    def get_float(self, section, key):
        """Read Setting."""
        return self.configfile.getfloat(section, key)

    def get_int(self, section, key):
        """Read Setting."""
        return self.configfile.getint(section, key)

    def save_config(self):
        """Save configuration file."""
        cfgfile = open(self.config_filename, "w", encoding="utf8")
        self.configfile.write(cfgfile)
        cfgfile.close()

    def gen_settings_dict(self):
        """Generate settings template to pass to flask."""
        settings = {}
        # FIXME - Change to boolean here and in HTML Templates
        settings["autorun"] = self.get_string("default", "autorun")
        settings["LED_COUNT"] = self.get_string("default", "led_count")
        # FIXME - Change to boolean here and in HTML Templates
        settings["legend"] = self.get_string("default", "legend")
        settings["max_wind_speed"] = self.get_string("metar", "max_wind_speed")
        settings["wx_update_interval"] = self.get_string("metar", "wx_update_interval")
        settings["metar_age"] = self.get_string("metar", "metar_age")
        settings["usetimer"] = self.get_string("schedule", "usetimer")
        settings["offhour"] = self.get_string("schedule", "offhour")
        settings["offminutes"] = self.get_string("schedule", "offminutes")
        settings["onhour"] = self.get_string("schedule", "onhour")
        settings["onminutes"] = self.get_string("schedule", "onminutes")
        settings["tempsleepon"] = self.get_string("schedule", "tempsleepon")
        settings["sleepmsg"] = self.get_string("schedule", "sleepmsg")
        settings["displayused"] = self.get_string("oled", "displayused")
        settings["oledused"] = self.get_string("oled", "oledused")
        settings["lcddisplay"] = self.get_string("oled", "lcddisplay")
        settings["numofdisplays"] = self.get_string("oled", "numofdisplays")
        settings["loglevel"] = self.get_string("default", "loglevel")
        settings["bright_value"] = self.get_string("lights", "bright_value")
        settings["hiwindblink"] = self.get_string("lights", "hiwindblink")
        settings["lghtnflash"] = self.get_string("lights", "lghtnflash")
        settings["rainshow"] = self.get_string("lights", "rainshow")
        settings["frrainshow"] = self.get_string("lights", "frrainshow")
        settings["snowshow"] = self.get_string("lights", "snowshow")
        settings["dustsandashshow"] = self.get_string("lights", "dustsandashshow")
        settings["fogshow"] = self.get_string("lights", "fogshow")
        settings["homeport"] = self.get_string("lights", "homeport")
        settings["homeport_pin"] = self.get_string("lights", "homeport_pin")
        settings["homeport_display"] = self.get_string("lights", "homeport_display")
        settings["dim_value"] = self.get_string("lights", "dim_value")
        settings["rgb_grb"] = self.get_string("lights", "rgb_grb")
        settings["rev_rgb_grb"] = self.get_string("lights", "rev_rgb_grb")
        settings["dimmed_value"] = self.get_string("lights", "dimmed_value")
        settings["legend_hiwinds"] = self.get_string("lights", "legend_hiwinds")
        settings["legend_lghtn"] = self.get_string("lights", "legend_lghtn")
        settings["legend_snow"] = self.get_string("lights", "legend_snow")
        settings["legend_rain"] = self.get_string("lights", "legend_rain")
        settings["legend_frrain"] = self.get_string("lights", "legend_frrain")
        settings["legend_dustsandash"] = self.get_string("lights", "legend_dustsandash")
        settings["legend_fog"] = self.get_string("lights", "legend_fog")
        settings["leg_pin_vfr"] = self.get_string("lights", "leg_pin_vfr")
        settings["leg_pin_mvfr"] = self.get_string("lights", "leg_pin_mvfr")
        settings["leg_pin_ifr"] = self.get_string("lights", "leg_pin_ifr")
        settings["leg_pin_lifr"] = self.get_string("lights", "leg_pin_lifr")
        settings["leg_pin_nowx"] = self.get_string("lights", "leg_pin_nowx")
        settings["leg_pin_hiwinds"] = self.get_string("lights", "leg_pin_hiwinds")
        settings["leg_pin_lghtn"] = self.get_string("lights", "leg_pin_lghtn")
        settings["leg_pin_snow"] = self.get_string("lights", "leg_pin_snow")
        settings["leg_pin_rain"] = self.get_string("lights", "leg_pin_rain")
        settings["leg_pin_frrain"] = self.get_string("lights", "leg_pin_frrain")
        settings["leg_pin_dustsandash"] = self.get_string(
            "lights", "leg_pin_dustsandash"
        )
        settings["leg_pin_fog"] = self.get_string("lights", "leg_pin_fog")
        settings["num2display"] = self.get_string("lights", "num2display")
        settings["exclusive_flag"] = self.get_string("lights", "exclusive_flag")
        settings["exclusive_list"] = self.get_string("lights", "exclusive_list")
        settings["abovekts"] = self.get_string("lights", "abovekts")
        settings["lcdpause"] = self.get_string("lights", "lcdpause")
        settings["rotyesno"] = self.get_string("oled", "rotyesno")
        settings["oledposorder"] = self.get_string("oled", "oledposorder")
        settings["oledpause"] = self.get_string("oled", "oledpause")
        settings["fontsize"] = self.get_string("oled", "fontsize")
        settings["offset"] = self.get_string("oled", "offset")
        settings["wind_numorarrow"] = self.get_string("oled", "wind_numorarrow")
        settings["boldhiap"] = self.get_string("oled", "boldhiap")
        settings["blankscr"] = self.get_string("oled", "blankscr")
        settings["border"] = self.get_string("oled", "border")
        settings["dimswitch"] = self.get_string("oled", "dimswitch")
        settings["dimmin"] = self.get_string("oled", "dimmin")
        settings["dimmax"] = self.get_string("oled", "dimmax")
        settings["invert"] = self.get_string("oled", "invert")
        settings["toginv"] = self.get_string("oled", "toginv")
        settings["scrolldis"] = self.get_string("oled", "scrolldis")
        settings["usewelcome"] = self.get_string("default", "usewelcome")
        settings["welcome"] = self.get_string("default", "welcome")
        settings["displaytime"] = self.get_string("oled", "displaytime")
        settings["displayip"] = self.get_string("oled", "displayip")
        settings["data_sw0"] = self.get_string("rotaryswitch", "data_sw0")
        settings["time_sw0"] = self.get_string("rotaryswitch", "time_sw0")
        settings["data_sw1"] = self.get_string("rotaryswitch", "data_sw1")
        settings["time_sw1"] = self.get_string("rotaryswitch", "time_sw1")
        settings["data_sw2"] = self.get_string("rotaryswitch", "data_sw2")
        settings["time_sw2"] = self.get_string("rotaryswitch", "time_sw2")
        settings["data_sw3"] = self.get_string("rotaryswitch", "data_sw3")
        settings["time_sw3"] = self.get_string("rotaryswitch", "time_sw3")
        settings["data_sw4"] = self.get_string("rotaryswitch", "data_sw4")
        settings["time_sw4"] = self.get_string("rotaryswitch", "time_sw4")
        settings["data_sw5"] = self.get_string("rotaryswitch", "data_sw5")
        settings["time_sw5"] = self.get_string("rotaryswitch", "time_sw5")
        settings["data_sw6"] = self.get_string("rotaryswitch", "data_sw6")
        settings["time_sw6"] = self.get_string("rotaryswitch", "time_sw6")
        settings["data_sw7"] = self.get_string("rotaryswitch", "data_sw7")
        settings["time_sw7"] = self.get_string("rotaryswitch", "time_sw7")
        settings["data_sw8"] = self.get_string("rotaryswitch", "data_sw8")
        settings["time_sw8"] = self.get_string("rotaryswitch", "time_sw8")
        settings["data_sw9"] = self.get_string("rotaryswitch", "data_sw9")
        settings["time_sw9"] = self.get_string("rotaryswitch", "time_sw9")
        settings["data_sw10"] = self.get_string("rotaryswitch", "data_sw10")
        settings["time_sw10"] = self.get_string("rotaryswitch", "time_sw10")
        settings["data_sw11"] = self.get_string("rotaryswitch", "data_sw11")
        settings["time_sw11"] = self.get_string("rotaryswitch", "time_sw11")

        settings["color_vfr"] = self.get_string("colors", "color_vfr")
        settings["color_mvfr"] = self.get_string("colors", "color_mvfr")
        settings["color_ifr"] = self.get_string("colors", "color_ifr")
        settings["color_lifr"] = self.get_string("colors", "color_lifr")
        settings["color_nowx"] = self.get_string("colors", "color_nowx")
        settings["color_black"] = self.get_string("colors", "color_black")
        settings["color_lghtn"] = self.get_string("colors", "color_lghtn")
        settings["color_snow1"] = self.get_string("colors", "color_snow1")
        settings["color_snow2"] = self.get_string("colors", "color_snow2")
        settings["color_rain1"] = self.get_string("colors", "color_rain1")
        settings["color_rain2"] = self.get_string("colors", "color_rain2")
        settings["color_frrain1"] = self.get_string("colors", "color_frrain1")
        settings["color_frrain2"] = self.get_string("colors", "color_frrain2")
        settings["color_dustsandash1"] = self.get_string("colors", "color_dustsandash1")
        settings["color_dustsandash2"] = self.get_string("colors", "color_dustsandash2")
        settings["color_fog1"] = self.get_string("colors", "color_fog1")
        settings["color_fog2"] = self.get_string("colors", "color_fog2")
        settings["color_homeport"] = self.get_string("colors", "color_homeport")
        settings["homeport_colors"] = self.get_string("colors", "homeport_colors")
        settings["fade_color1"] = self.get_string("colors", "fade_color1")
        settings["allsame_color1"] = self.get_string("colors", "allsame_color1")
        settings["allsame_color2"] = self.get_string("colors", "allsame_color2")
        settings["shuffle_color1"] = self.get_string("colors", "shuffle_color1")
        settings["shuffle_color2"] = self.get_string("colors", "shuffle_color2")
        settings["radar_color1"] = self.get_string("colors", "radar_color1")
        settings["radar_color2"] = self.get_string("colors", "radar_color2")
        settings["circle_color1"] = self.get_string("colors", "circle_color1")
        settings["circle_color2"] = self.get_string("colors", "circle_color2")
        settings["square_color1"] = self.get_string("colors", "square_color1")
        settings["square_color2"] = self.get_string("colors", "square_color2")
        settings["updn_color1"] = self.get_string("colors", "updn_color1")
        settings["updn_color2"] = self.get_string("colors", "updn_color2")
        settings["morse_color1"] = self.get_string("colors", "morse_color1")
        settings["morse_color2"] = self.get_string("colors", "morse_color2")
        settings["rabbit_color1"] = self.get_string("colors", "rabbit_color1")
        settings["rabbit_color2"] = self.get_string("colors", "rabbit_color2")
        settings["checker_color1"] = self.get_string("colors", "checker_color1")
        settings["checker_color2"] = self.get_string("colors", "checker_color2")
        return settings

    def parse_config_input(self, form_data):
        """Parse settings data input."""
        # FIXME - Change to boolean here and in HTML Templates
        self.set_string("default", "autorun", form_data["autorun"])
        self.set_string("default", "led_count", form_data["LED_COUNT"])
        # FIXME - Change to boolean here and in HTML Templates
        self.set_string("default", "legend", form_data["legend"])
        self.set_string("metar", "max_wind_speed", form_data["max_wind_speed"])
        self.set_string("metar", "wx_update_interval", form_data["wx_update_interval"])
        self.set_string("metar", "metar_age", form_data["metar_age"])
        self.set_string("schedule", "usetimer", form_data["usetimer"])
        self.set_string("schedule", "offhour", form_data["offhour"])
        self.set_string("schedule", "offminutes", form_data["offminutes"])
        self.set_string("schedule", "onhour", form_data["onhour"])
        self.set_string("schedule", "onminutes", form_data["onminutes"])
        self.set_string("schedule", "tempsleepon", form_data["tempsleepon"])
        self.set_string("schedule", "sleepmsg", form_data["sleepmsg"])
        self.set_string("oled", "displayused", form_data["displayused"])
        self.set_string("oled", "oledused", form_data["oledused"])
        self.set_string("oled", "lcddisplay", form_data["lcddisplay"])
        self.set_string("oled", "numofdisplays", form_data["numofdisplays"])
        self.set_string("default", "loglevel", form_data["loglevel"])
        self.set_string("lights", "bright_value", form_data["bright_value"])
        self.set_string("lights", "hiwindblink", form_data["hiwindblink"])
        self.set_string("lights", "lghtnflash", form_data["lghtnflash"])
        self.set_string("lights", "rainshow", form_data["rainshow"])
        self.set_string("lights", "frrainshow", form_data["frrainshow"])
        self.set_string("lights", "snowshow", form_data["snowshow"])
        self.set_string("lights", "dustsandashshow", form_data["dustsandashshow"])
        self.set_string("lights", "fogshow", form_data["fogshow"])
        self.set_string("lights", "homeport", form_data["homeport"])
        self.set_string("lights", "homeport_pin", form_data["homeport_pin"])
        self.set_string("lights", "homeport_display", form_data["homeport_display"])
        self.set_string("lights", "dim_value", form_data["dim_value"])
        self.set_string("lights", "rgb_grb", form_data["rgb_grb"])
        self.set_string("lights", "rev_rgb_grb", form_data["rev_rgb_grb"])
        self.set_string("lights", "dimmed_value", form_data["dimmed_value"])
        self.set_string("lights", "legend_hiwinds", form_data["legend_hiwinds"])
        self.set_string("lights", "legend_lghtn", form_data["legend_lghtn"])
        self.set_string("lights", "legend_snow", form_data["legend_snow"])
        self.set_string("lights", "legend_rain", form_data["legend_rain"])
        self.set_string("lights", "legend_frrain", form_data["legend_frrain"])
        self.set_string("lights", "legend_dustsandash", form_data["legend_dustsandash"])
        self.set_string("lights", "legend_fog", form_data["legend_fog"])
        self.set_string("lights", "leg_pin_vfr", form_data["leg_pin_vfr"])
        self.set_string("lights", "leg_pin_mvfr", form_data["leg_pin_mvfr"])
        self.set_string("lights", "leg_pin_ifr", form_data["leg_pin_ifr"])
        self.set_string("lights", "leg_pin_lifr", form_data["leg_pin_lifr"])
        self.set_string("lights", "leg_pin_nowx", form_data["leg_pin_nowx"])
        self.set_string("lights", "leg_pin_hiwinds", form_data["leg_pin_hiwinds"])
        self.set_string("lights", "leg_pin_lghtn", form_data["leg_pin_lghtn"])
        self.set_string("lights", "leg_pin_snow", form_data["leg_pin_snow"])
        self.set_string("lights", "leg_pin_rain", form_data["leg_pin_rain"])
        self.set_string("lights", "leg_pin_frrain", form_data["leg_pin_frrain"])
        self.set_string(
            "lights", "leg_pin_dustsandash", form_data["leg_pin_dustsandash"]
        )
        self.set_string("lights", "leg_pin_fog", form_data["leg_pin_fog"])
        self.set_string("lights", "num2display", form_data["num2display"])
        self.set_string("lights", "exclusive_flag", form_data["exclusive_flag"])
        self.set_string("lights", "exclusive_list", form_data["exclusive_list"])
        self.set_string("lights", "abovekts", form_data["abovekts"])
        self.set_string("lights", "lcdpause", form_data["lcdpause"])
        self.set_string("oled", "rotyesno", form_data["rotyesno"])
        self.set_string("oled", "oledposorder", form_data["oledposorder"])
        self.set_string("oled", "oledpause", form_data["oledpause"])
        self.set_string("oled", "fontsize", form_data["fontsize"])
        self.set_string("oled", "offset", form_data["offset"])
        self.set_string("oled", "wind_numorarrow", form_data["wind_numorarrow"])
        self.set_string("oled", "boldhiap", form_data["boldhiap"])
        self.set_string("oled", "blankscr", form_data["blankscr"])
        self.set_string("oled", "border", form_data["border"])
        self.set_string("oled", "dimswitch", form_data["dimswitch"])
        self.set_string("oled", "dimmin", form_data["dimmin"])
        self.set_string("oled", "dimmax", form_data["dimmax"])
        self.set_string("oled", "invert", form_data["invert"])
        self.set_string("oled", "toginv", form_data["toginv"])
        self.set_string("oled", "scrolldis", form_data["scrolldis"])
        self.set_string("default", "usewelcome", form_data["usewelcome"])
        self.set_string("default", "welcome", form_data["welcome"])
        self.set_string("oled", "displaytime", form_data["displaytime"])
        self.set_string("oled", "displayip", form_data["displayip"])
        self.set_string("rotaryswitch", "data_sw0", form_data["data_sw0"])
        self.set_string("rotaryswitch", "time_sw0", form_data["time_sw0"])
        self.set_string("rotaryswitch", "data_sw1", form_data["data_sw1"])
        self.set_string("rotaryswitch", "time_sw1", form_data["time_sw1"])
        self.set_string("rotaryswitch", "data_sw2", form_data["data_sw2"])
        self.set_string("rotaryswitch", "time_sw2", form_data["time_sw2"])
        self.set_string("rotaryswitch", "data_sw3", form_data["data_sw3"])
        self.set_string("rotaryswitch", "time_sw3", form_data["time_sw3"])
        self.set_string("rotaryswitch", "data_sw4", form_data["data_sw4"])
        self.set_string("rotaryswitch", "time_sw4", form_data["time_sw4"])
        self.set_string("rotaryswitch", "data_sw5", form_data["data_sw5"])
        self.set_string("rotaryswitch", "time_sw5", form_data["time_sw5"])
        self.set_string("rotaryswitch", "data_sw6", form_data["data_sw6"])
        self.set_string("rotaryswitch", "time_sw6", form_data["time_sw6"])
        self.set_string("rotaryswitch", "data_sw7", form_data["data_sw7"])
        self.set_string("rotaryswitch", "time_sw7", form_data["time_sw7"])
        self.set_string("rotaryswitch", "data_sw8", form_data["data_sw8"])
        self.set_string("rotaryswitch", "time_sw8", form_data["time_sw8"])
        self.set_string("rotaryswitch", "data_sw9", form_data["data_sw9"])
        self.set_string("rotaryswitch", "time_sw9", form_data["time_sw9"])
        self.set_string("rotaryswitch", "data_sw10", form_data["data_sw10"])
        self.set_string("rotaryswitch", "time_sw10", form_data["time_sw10"])
        self.set_string("rotaryswitch", "data_sw11", form_data["data_sw11"])
        self.set_string("rotaryswitch", "time_sw11", form_data["time_sw11"])

        self.set_string("colors", "color_vfr", form_data["color_vfr"])
        self.set_string("colors", "color_mvfr", form_data["color_mvfr"])
        self.set_string("colors", "color_ifr", form_data["color_ifr"])
        self.set_string("colors", "color_lifr", form_data["color_lifr"])
        self.set_string("colors", "color_nowx", form_data["color_nowx"])
        self.set_string("colors", "color_black", form_data["color_black"])
        self.set_string("colors", "color_lghtn", form_data["color_lghtn"])
        self.set_string("colors", "color_snow1", form_data["color_snow1"])
        self.set_string("colors", "color_snow2", form_data["color_snow2"])
        self.set_string("colors", "color_rain1", form_data["color_rain1"])
        self.set_string("colors", "color_rain2", form_data["color_rain2"])
        self.set_string("colors", "color_frrain1", form_data["color_frrain1"])
        self.set_string("colors", "color_frrain2", form_data["color_frrain2"])
        self.set_string("colors", "color_dustsandash1", form_data["color_dustsandash1"])
        self.set_string("colors", "color_dustsandash2", form_data["color_dustsandash2"])
        self.set_string("colors", "color_fog1", form_data["color_fog1"])
        self.set_string("colors", "color_fog2", form_data["color_fog2"])
        self.set_string("colors", "color_homeport", form_data["color_homeport"])
        self.set_string("colors", "homeport_colors", form_data["homeport_colors"])
        self.set_string("colors", "fade_color1", form_data["fade_color1"])
        self.set_string("colors", "allsame_color1", form_data["allsame_color1"])
        self.set_string("colors", "allsame_color2", form_data["allsame_color2"])
        self.set_string("colors", "shuffle_color1", form_data["shuffle_color1"])
        self.set_string("colors", "shuffle_color2", form_data["shuffle_color2"])
        self.set_string("colors", "radar_color1", form_data["radar_color1"])
        self.set_string("colors", "radar_color2", form_data["radar_color2"])
        self.set_string("colors", "circle_color1", form_data["circle_color1"])
        self.set_string("colors", "circle_color2", form_data["circle_color2"])
        self.set_string("colors", "square_color1", form_data["square_color1"])
        self.set_string("colors", "square_color2", form_data["square_color2"])
        self.set_string("colors", "updn_color1", form_data["updn_color1"])
        self.set_string("colors", "updn_color2", form_data["updn_color2"])
        self.set_string("colors", "morse_color1", form_data["morse_color1"])
        self.set_string("colors", "morse_color2", form_data["morse_color2"])
        self.set_string("colors", "rabbit_color1", form_data["rabbit_color1"])
        self.set_string("colors", "rabbit_color2", form_data["rabbit_color2"])
        self.set_string("colors", "checker_color1", form_data["checker_color1"])
        self.set_string("colors", "checker_color2", form_data["checker_color2"])
