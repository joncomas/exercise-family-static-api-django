from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from api.family_datastructure import Family
import json
from api.family_datastructure import *

# initialize a 'Doe' family
family = Family(last_name='Doe')
"""
The MembersView will contain the logic on how to:
 GET, POST, PUT or delete family members
"""


class MembersView(APIView):
    def get(self, request, member_id=None):
        # fill this method and update the return
        if member_id is not None:
            CogeMiembro = family.get_member(member_id)
            return Response(CogeMiembro, status=status.HTTP_200_OK)
        else:
            CogeMiembro = family.get_all_members()
        return Response(CogeMiembro, status=status.HTTP_200_OK)

    def post(self, request):
        # fill this method and update the return
        if request is not None:
            AgregaMienbro = family.add_member(request.data)
        return Response(AgregaMienbro, status=status.HTTP_200_OK)

    def put(self, request, member_id=None):
        # fill this method and update the return
        if request and member_id is not None:
            PonerMienbro = family.update_member(member_id, request.data)
        return Response(PonerMienbro, status=status.HTTP_200_OK)

    def delete(self, request, member_id=None):
        # fill this method and update the return
        if member_id is not None:
            family.delete_member(member_id)
        return Response({"status": "Borrado"}, status=status.HTTP_200_OK)
