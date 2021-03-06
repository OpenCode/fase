#!/usr/bin/python

# ######################################################################
#
#  FaSE - Facebook Separated Environment
#
#  Copyright 2014 Francesco OpenCode Apruzzese <opencode@e-ware.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ######################################################################


# ----- Hide ads

jsRemoveAdsById = """
    var ads = ["pagelet_ego_pane", "pagelet_side_ads"];
    for (var i in ads) {
        ad = document.getElementById(ads[i]);
        if (ad) {
            ad.parentNode.removeChild(ad);
        }
    }
"""

jsRemoveAdsByClass = """
    var class_names = ["ego_section"];
    for (var name in class_names) {
        var ads = document.getElementsByClassName(class_names[name]);
        if (ads) {
            for (var ad = 0, length = ads.length; ad < length; ad++) {
                ads[ad].parentNode.removeChild(ads[ad]);
            }
        }
    }
"""
