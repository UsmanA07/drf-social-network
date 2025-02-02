from rest_framework.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    return f'avatar/{instance.id}/{file}'


def validated_size_avatar(file_obj):
    limit_size_mb = 2
    if file_obj.size > limit_size_mb * 1024 * 1024:
        raise ValidationError(f'Max size file: {limit_size_mb}')


def validated_phone_number(num: int):
    if str(num)[0] == '1':
        print('validated')
    else:
        print('not validated')
    print(num)
