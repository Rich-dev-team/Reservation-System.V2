# from django.contrib.auth.models import User
# from django.contrib.auth.backends import ModelBackend
from .models import Account, Staff
from .serializers import Acc_Serializer
from django.db import transaction, DatabaseError
from functools import wraps


# def login_required(fun):
    # @wrap(fun)
    # def wrapper(request,*args, **kwargs):
    #     if check_login():
    #         return 403


def ClientAuthentication(social_id, social_app):  # Account Check Auth
    try:
        if (social_id == None) or (social_app == None):  # Using PC or No social login
            return None
        else:   # parameter not None
            with transaction.atomic():  # transaction
                queryset = Account.objects.select_for_update().get(
                    social_id=social_id,
                    social_app=social_app,
                )

                serializer = Acc_Serializer(queryset)
                return serializer.data
    except Account.DoesNotExist:  # Account Not Exist
        return False
    except Exception as e:
        return {'error': e}


def StaffAuthentication(social_id, social_app):  # staff account checking
    try:
        if (social_id == None) or (social_app == None):  # Using PC or No social login
            return None
        else:   # parameter not None
            queryset = Staff.objects.only(
                'staff_id',
                'staff_name',
                'staff_level',
                'staff_ended',
                'social_id',
                'social_app',
            ).get(
                social_id=social_id,
                social_app=social_app,
            )
            serializer = Acc_Serializer(queryset)
            return serializer.data

    except Account.DoesNotExist:  # Account Not Exist
        return False
    except Exception as e:
        return {'error': e}
