#!/usr/bin/python
#
# uptime.py: Basic JabberBot example with command prefix
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Homepage: http://thp.io/2007/python-jabberbot/
#

import subprocess
import sys

from jabberbot import *

class UptimeBot(JabberBot):
    @botcmd
    def uptime(self, mess, args):
        """Get current uptime information"""
        return subprocess.check_output('uptime')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print >>sys.stderr, """
        Usage: %s <jid> <password>
        """ % sys.argv[0]

    username, password = sys.argv[1:]
    uptime_bot = UptimeBot(username, password, command_prefix='.')
    uptime_bot.serve_forever()

