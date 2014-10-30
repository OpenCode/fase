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


# -------
# IMPORTS
# -------
from datetime import datetime

# ---------
# CONSTANTS
# ---------
LOG_INFO = 0
LOG_WARNING = 1
LOG_ERROR = 2
LOG_SYSTEM = 3

LOG_FORMAT = {
    LOG_INFO: 'INFO',
    LOG_WARNING: 'WARN',
    LOG_ERROR: 'ERRR',
    LOG_SYSTEM: 'SYST',
    }


def base_log(message, log_type=LOG_INFO):
    return '[%s] %s %s' % (LOG_FORMAT[log_type],
                           datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                           message)


def info_log(message):
    print base_log(message, LOG_INFO)


def warning_log(message):
    print base_log(message, LOG_WARNING)


def error_log(message):
    print base_log(message, LOG_ERROR)


def system_log(message):
    print base_log(message, LOG_SYSTEM)
