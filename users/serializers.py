from rest_framework import serializers


'''field参数'''
# 1.read_only
read_only=True
# 2.write_only
write_only=True
# 3.required:该字段是必需的，不能为空
required=True
# 4.allow_null/allow_blank：该字段允许为null
allow_null = True

# 5.label:标签，用于对字段显示设置
# 6.help_text:对字段进行解释的一段文本，用于提示
# 7.style:说明字段的类型
# 8.error_messages: 字段出错时，信息提示

# user/models.py
# class User(AbstractUser):
# phone = models.CharField('手机号',max_length=20)
# img = models.ImageField(upload_to='user',null=True)
# nick_name = models.CharField('昵称',max_length=20)
# address = models.CharField('地址',max_length=255)

class UserInfoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)  # 普通字段，设置id为只读，不能修改
    username = serializers.CharField(min_length=3, max_length=20,
                                     error_messages={"required": "该字段必填"})  # 普通字段最小三最大20，字段出粗时提醒该字段必填
    img = serializers.ImageField(required=False)  # 不是必填字段
    nick_name = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=255)
    xxx = serializers.SerializerMethodField(read_only=True)  # 自定义显示（显示多对多）

    class Meta:
        model = User

    # 自定义显示多对多字段
    def get_xxx(self, row):  # get_字段名
        '''row：就是传过来的User表的对象'''
        users = row.username  # 获取用户名
        return users

    # 自定义创建语法，ser.save()执行，就会立刻调用create方法用来创建数据
    def create(self, validated_data):
        '''validated_data:表单或者vue请求携带的json：{"username": "zhangsan", "password": "123456"}'''
        return User.objects.create(**validated_data)


# 自定义更新方法
def update(self, instance, validated_data):
    '''
    instance:查询的对象
    validated_data : postman提交的json数据：{"username": "zhangsan", "password": "123456"}
    '''
    if validated_data.get("username"):
        instance.username = validated_data["username"]
    instance.save()
    return instance


# 定义单一字段验证的方法：  validate_字段名
def validate_name(self, value):
    if value == "root":
        raise serializers.ValidatetionError('不能创建root管理员账号')


# 定义多字段验证方法
def validate(self, attrs):
    if attrs.get("username") == 'admin':
        raise serializers.ValidationError('不能创建admin用户')
    return attrs