FROM ubuntu:18.04

USER root

RUN apt-get update && \
    apt-get -y install sudo git python-pip autoconf bison build-essential pkg-config bison flex autoconf unzip automake libtool make git python2.7 python-pip sqlite3 cmake python3 python3-pip wget
RUN pip install flask flask-login pyserial pymodbus


WORKDIR /home/
RUN git clone https://github.com/thiagoralves/ScadaBR_Installer.git
WORKDIR /home/ScadaBR_Installer/
RUN sudo ./install_scadabr.sh linux

COPY run.sh /home/ScadaBR_Installer/
RUN sudo chmod +x run.sh
RUN mkdir selenium


RUN apt-get -y install adwaita-icon-theme at-spi2-core dconf-gsettings-backend dconf-service fontconfig fontconfig-config fonts-liberation glib-networking glib-networking-common glib-networking-services \
  gsettings-desktop-schemas gtk-update-icon-cache hicolor-icon-theme humanity-icon-theme libasound2 libasound2-data libatk-bridge2.0-0 libatk1.0-0 libatk1.0-data libatspi2.0-0 libauthen-sasl-perl \
  libavahi-client3 libavahi-common-data libavahi-common3 libcairo-gobject2 libcairo2 libcolord2 libcroco3 libcups2 libdata-dump-perl libdatrie1 libdconf1 libdrm-amdgpu1 libdrm-common libdrm-intel1 \
  libdrm-nouveau2 libdrm-radeon1 libdrm2 libelf1 libencode-locale-perl libepoxy0 libfile-basedir-perl libfile-desktopentry-perl libfile-listing-perl libfile-mimeinfo-perl libfont-afm-perl \
  libfontconfig1 libfontenc1 libfreetype6 libgbm1 libgdk-pixbuf2.0-0 libgdk-pixbuf2.0-bin libgdk-pixbuf2.0-common libgl1 libgl1-mesa-dri libgl1-mesa-glx libglapi-mesa libglvnd0 libglx-mesa0 libglx0 \
  libgraphite2-3 libgtk-3-0 libgtk-3-bin libgtk-3-common libharfbuzz0b libhtml-form-perl libhtml-format-perl libhtml-parser-perl libhtml-tagset-perl libhtml-tree-perl libhttp-cookies-perl \
  libhttp-daemon-perl libhttp-date-perl libhttp-message-perl libhttp-negotiate-perl libice6 libio-html-perl libio-socket-ssl-perl libipc-system-simple-perl libjbig0 libjpeg-turbo8 libjpeg8 \
  libjson-glib-1.0-0 libjson-glib-1.0-common liblcms2-2 libllvm10 liblwp-mediatypes-perl liblwp-protocol-https-perl libmailtools-perl libnet-dbus-perl libnet-http-perl libnet-smtp-ssl-perl \
  libnet-ssleay-perl libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libpangoft2-1.0-0 libpciaccess0 libpixman-1-0 libpng16-16 libproxy1v5 librest-0.7-0 librsvg2-2 librsvg2-common libsensors4 \
  libsm6 libsoup-gnome2.4-1 libsoup2.4-1 libtext-iconv-perl libthai-data libthai0 libtie-ixhash-perl libtiff5 libtimedate-perl libtry-tiny-perl liburi-perl libwayland-client0 libwayland-cursor0 \
  libwayland-egl1 libwayland-server0 libwww-perl libwww-robotrules-perl libx11-protocol-perl libx11-xcb1 libxaw7 libxcb-dri2-0 libxcb-dri3-0 libxcb-glx0 libxcb-present0 libxcb-render0 libxcb-shape0 \
  libxcb-shm0 libxcb-sync1 libxcomposite1 libxcursor1 libxdamage1 libxfixes3 libxft2 libxi6 libxinerama1 libxkbcommon0 libxml-parser-perl libxml-twig-perl libxml-xpathengine-perl libxmu6 libxpm4 \
  libxrandr2 libxrender1 libxshmfence1 libxt6 libxtst6 libxv1 libxxf86dga1 libxxf86vm1 perl-openssl-defaults ubuntu-mono ucf x11-common x11-utils x11-xserver-utils xdg-utils xkb-data

RUN apt-get -y install nginx
COPY default /etc/nginx/sites-available/default

#RUN apt-get -y install fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 libgbm1 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 libxrandr2 libxshmfence1 xdg-utils

WORKDIR /home/selenium

COPY host.sh /home/selenium

COPY init.sh /home/selenium
COPY chromedriver /home/selenium
COPY loaddata.py /home/selenium
COPY json2.txt /home/selenium
COPY dataHMI.txt /home/selenium
COPY google-chrome-stable_current_amd64.deb /home/selenium/

RUN sudo dpkg -i /home/selenium/google-chrome-stable_current_amd64.deb && \
    sudo chmod +x /home/selenium/chromedriver && \
    sudo apt install python3-pip
RUN sudo mv /home/selenium/chromedriver /usr/local/share/chromedriver && \
    sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver && \
    pip3 install selenium
RUN sudo chmod +x loaddata.py

WORKDIR /home/ScadaBR_Installer/
RUN sudo ./update_scadabr.sh

#RUN sudo sudo /opt/tomcat6/apache-tomcat-6.0.53/bin/startup.sh

WORKDIR /home/selenium
#RUN sudo python3 loaddata.py

EXPOSE 502
EXPOSE 8080
EXPOSE 9090

CMD ["/bin/bash", "/home/selenium/init.sh"] && ["nginx", "-g", "daemon off;"]