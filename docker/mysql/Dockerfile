FROM mysql:5.7-debian

RUN apt-get update -y && \
    apt-get install -y locales && \
    rm -rf /var/lib/apt/lists/* && \
    echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen ja_JP.UTF-8

COPY etc/mysql/conf.d/charset.cnf /etc/mysql/conf.d/charset.cnf
RUN chmod 644 /etc/mysql/conf.d/charset.cnf
COPY etc/mysql/conf.d/log.cnf /etc/mysql/conf.d/log.cnf
RUN chmod 644 /etc/mysql/conf.d/log.cnf
