# -*- coding: utf-8 -*-
# Copyright 2017-2018 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
"""
Defines views for |SupplyOrders| using the Django REST framework.

==============================  ===========================================
Class                           Description
==============================  ===========================================
:class:`~SupplyOrderViewSet`    |CustomModelViewSet| for |SupplyOrders|.
==============================  ===========================================

"""

# local
from cyphon.views import CustomModelViewSet
from .models import SupplyOrder
from .serializers import SupplyOrderSerializer


class SupplyOrderViewSet(CustomModelViewSet):
    """REST API views for SupplyOrders."""

    queryset = SupplyOrder.objects.all()
    custom_filter_backends = ['cyphon.filters.UserFilterBackend']
    serializer_class = SupplyOrderSerializer