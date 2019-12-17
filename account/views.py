from rest_framework import generics, mixins, viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from account.models import User
from account.serializers import UserSerializer, UserCreateSerializer, UserAvatarSerializer


class UserListView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin,
                   generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class UserDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class UserImgView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = UserAvatarSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class UserRegistView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin,
                     generics.GenericAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    # 用户注册成功后，会在 User 表中生成一条记录；如果想要在生成 User记录的同时，生成一个 token ，
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # 在此处生成 token
        res_dict = {'username': serializer.data['username']}
        payload = jwt_payload_handler(user)  # user 是 User 表中生成的一条新记录
        res_dict["token"] = jwt_encode_handler(payload)  # jwt_encode_handler(payload) 生成 token；

        headers = self.get_success_headers(serializer.data)
        return Response(res_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = User(username=serializer.data['username'])
        user.set_password(serializer.data.get('password'))
        user.save()
        return user  # 把保存的 User 对象返回


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'partial_update':
            return UserAvatarSerializer
        else:
            return super().get_serializer_class()
