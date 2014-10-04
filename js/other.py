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


# ----- Change login page
jsChangeLoginPage = """ 
    var div_parents = document.getElementsByClassName('_5iyy');
    var e = document.createElement('div');
    e.setAttribute('class', '_5iyx')
    e.innerHTML = 'You Are using <a href="https://github.com/OpenCode/fase">FASE</a> and this is great!';
    div_parents[0].insertBefore(e);
    """

