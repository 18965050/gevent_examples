## 说明

### 版本说明
- python: 3.5.1
- gevent: 1.1.1
- greenlet: 0.4.10

### 例外

- g09_clean_shutdown.py: gevent1.0以上的版本中没有gevent.shutdown()方法, 此脚本执行不了
- g24_subprocess.py/g25_read_write.py: 只能在Unix/Linux中执行
