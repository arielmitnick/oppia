# coding: utf-8
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Models for Oppia statistics."""

__author__ = 'Sean Lip'

from apps.base_model.models import BaseModel

from google.appengine.ext import ndb


class Counter(BaseModel):
    """An integer-valued counter."""
    # The name of the property.
    name = ndb.StringProperty()
    # The value of the property.
    value = ndb.IntegerProperty(default=0)
    # When this counter was first created.
    created = ndb.DateTimeProperty(auto_now_add=True)
    # When this counter was last incremented.
    last_updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_value_by_id(cls, key):
        counter = Counter.get_by_id(key)
        return counter.value if counter else 0


class Journal(BaseModel):
    """A list of values."""
    # The name of the list
    name = ndb.StringProperty()
    # The list of values
    values = ndb.StringProperty(repeated=True)
    # When this counter was first created.
    created = ndb.DateTimeProperty(auto_now_add=True)
    # When this counter was last updated.
    last_updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_value_count_by_id(cls, key):
        journal = Journal.get_by_id(key)
        return len(journal.values) if journal else 0
