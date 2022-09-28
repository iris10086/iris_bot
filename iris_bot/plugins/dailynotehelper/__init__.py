import schedule
import datetime
import os
from time import sleep
from . import notifiers
from .__banner__ import banner
from .utils import *
from .utils import _
from .config import config
from .getinfo.praseinfo import *
from .getinfo.mihoyo import Yuanshen
from .getinfo.hoyolab import Genshin


def start(cookies: list, server: str) -> [str]:
    result = []
    for index, cookie in enumerate(cookies):
        log.info(
            _('🗝️ 当前配置了{}个账号，正在执行第{}个').format(
                os.environ['ACCOUNT_NUM'], os.environ['ACCOUNT_INDEX']
            )
        )
        log.info('-------------------------')
        os.environ['ACCOUNT_INDEX'] = str(int(os.environ['ACCOUNT_INDEX']) + 1)
        client = Yuanshen(cookie, config.RUN_ENV) if server == 'cn' else Genshin(cookie)
        roles_info = client.roles_info
        if isinstance(roles_info, list):
            log.info(
                _('获取到{0}的{1}个角色...').format(
                    (_('国服') if server == 'cn' else _('国际服')), len(roles_info)
                )
            )
            for i, role in enumerate(roles_info):
                log.info(
                    (_('第{}个角色，{} {}')).format(
                        i + 1, role['game_uid'], role['nickname']
                    )
                )
                if role['game_uid'] in str(config.EXCLUDE_UID):
                    log.info(_('跳过该角色'))
                else:
                    dailynote_info, message = client.prase_dailynote_info(role)
                    if not dailynote_info:
                        status = (_('获取UID: {} 数据失败！')).format(role['game_uid'])
                        message = _('请查阅运行日志获取详细原因。')
                    result.append(message)
        else:
            log.error(roles_info)
            status = _('获取米游社角色信息失败！')
            message = roles_info
            result.append(message)
        log.info(f'-------------------------')
    return result


def run_once() -> [str]:
    os.environ['ACCOUNT_INDEX'] = '1'
    os.environ['ACCOUNT_NUM'] = str(len(config.COOKIE + config.COOKIE_HOYOLAB))
    res = []
    if len(config.COOKIE):
        res.extend(start(config.COOKIE, 'cn'))
    if len(config.COOKIE_HOYOLAB):
        res.extend(start(config.COOKIE_HOYOLAB, 'os'))
    log.info(_('本轮运行结束，等待下次检查...'))
    return res


def run() -> None:
    log.info(banner)
    run_once()
    schedule.every(config.CHECK_INTERVAL).minutes.do(run_once)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    run()
