VERSION=$1

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
       libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
       libncurses5-dev libncursesw5-dev xz-utils tk-dev

wget https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz
tar xvf Python-${VERSION}.tgz
cd Python-${VERSION}

./configure --enable-optimizations
sudo make -j 8 \
    PROFILE_TASK='-m test.regrtest --pgo \
        test_array \
        test_base64 \
        test_binascii \
        test_binhex \
        test_binop \
        test_bytes \
        test_c_locale_coercion \
        test_class \
        test_cmath \
        test_codecs \
        test_compile \
        test_complex \
        test_csv \
        test_decimal \
        test_dict \
        test_float \
        test_fstring \
        test_hashlib \
        test_io \
        test_iter \
        test_json \
        test_long \
        test_math \
        test_memoryview \
        test_pickle \
        test_re \
        test_set \
        test_slice \
        test_struct \
        test_threading \
        test_time \
        test_traceback \
        test_unicode \
    '
sudo make altinstall
sudo rm -r -f Python-${VERSION}*