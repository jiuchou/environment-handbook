requests.utils

@contextlib.contextmanager
def set_environ(env_name, value)


def _set_env(cmds):
    """Set the environment variable that is similar to `cmds`

    Parse parameters, `cmds` decode value form:
        'export A=DASF && export B=adfasd; export C=qqq'

    If `cmd` is None, do nothing"""
    if not cmds:
        return

    # python3 的 base64 解密后是 byte 类型，无法直接使用 replace 方法
    if sys.version_info.major == 3:
        cmds = base64.b64decode(cmds).decode().replace("&&", "\n")
    else:
        cmds = base64.b64decode(cmds).replace("&&", "\n")
    if platform.system() == "Windows":
        pre_env = "set"
        split_break = ";"
    else:
        pre_env = "export"
        split_break = ":"
        cmds = cmds.replace(";", "\n")
    LOG.info("cmds: %s", cmds)

    # env_path = os.environ['PATH']
    for cmd in cmds.split("\n"):
        if cmd.strip().startswith(pre_env):
            # 使用 strip 的时候，如果是 export JRE_HOME=$JAVA_HOME/jre ，则结果
            # 为 JRE_HOME=$JAVA_HOME/j ，使用 re 模块进行替换
            key = re.sub(pre_env + '| ', '', cmd).split('=')[0]
            value = re.sub(pre_env + '| ', '', cmd).split('=')[1]
            # 如果 value 中是用 `$` 或者 `%`，则替换成环境变量中的值，不仅限于
            # PATH 变量
            # if key == "PATH":
            #     value = re.sub("%PATH%|\$PATH|\${PATH}", env_path, value)
            # os.environ[key] = value
            env_keys = []
            # if '$' in value or '%' in value:
            #     for v in value.split(split_break):
            for v in value.split(split_break):
                if '$' in v or '%' in v:
                    env_key = v.split('/')[0].strip('$|{|}|%')
                    env_keys.append(env_key)
            for env_key in env_keys:
                LOG.debug(env_key)
                LOG.debug(value)
                # 如果存在不正确的环境变量，下载代码的时候会失败，因此如果环境变量不正确此处直接异常退出
                # windows 场景的用户环境变量可能使用小写
                if platform.system() == "Windows":
                    if env_key.upper() not in os.environ.keys():
                        LOG.warning("No environment variable: %s", env_key)
                        # continue
                        # raise Exception("No environment variable: {}".format(env_key))
                else:
                    if env_key not in os.environ.keys():
                        LOG.warning("No environment variable: %s", env_key)
                        # raise Exception("No environment variable: {}".format(env_key))
                value = value.replace('%' + env_key + '%', os.environ.get(env_key, ''))
                value = value.replace('$' + env_key, os.environ.get(env_key, ''))
                value = value.replace('${' + env_key + '}', os.environ.get(env_key, ''))
            os.environ[key] = value
            LOG.info("key=value: %s=%s", key, value)
    LOG.info("set env successful")

