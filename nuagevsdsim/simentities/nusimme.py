# BSD 3-Clause License
#
# Copyright (c) 2017, Philippe Dellaert
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
me
"""
import logging
import uuid
import time

from flask_restful import Resource
from nuagevsdsim.common.utils import NUAGE_API_DATA


class NUSimMe(Resource):

    def get(self):

        logging.debug('me get request received')
        result = [
            {
                "userName": NUAGE_API_DATA['USERS'][NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']].user_name,
                "mobileNumber": None,
                "flowCollectionEnabled": False,
                "APIKey": str(uuid.uuid1()),
                "firstName": NUAGE_API_DATA['USERS'][NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']].first_name,
                "statisticsEnabled": False,
                "APIKeyExpiry": int((time.time()+86400)*1000),
                "lastName": NUAGE_API_DATA['USERS'][NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']].last_name,
                "enterpriseID": NUAGE_API_DATA['ROOT_UUIDS']['csp_enterprise'],
                "ID": NUAGE_API_DATA['ROOT_UUIDS']['csproot_user'],
                "entityScope": None,
                "avatarType": None,
                "enterpriseName": NUAGE_API_DATA['ENTERPRISES'][NUAGE_API_DATA['ROOT_UUIDS']['csp_enterprise']].name,
                "role": "CSPROOT",
                "statsTSDBServerAddress": None,
                "avatarData": None,
                "licenseCapabilities": [],
                "externalId": None,
                "password": None,
                "email": NUAGE_API_DATA['USERS'][NUAGE_API_DATA['ROOT_UUIDS']['csproot_user']].email,
                "externalID": None
            }
        ]
        return result


