<h1>Content Aware Auto Brightness</h1>
<p>
  A simple Python script to change brightness based on the content on your screen.
</p>
<p>
  Currently for Windows and MacOS. (working on Linux)
</p>

<h2>To Install</h2>
<ul>
  <li>Clone this repository.</li>
  <li>Run <code>pip install -r requirements.txt</code>.</li>
  <li>Run <code>python sys_tray.py</code>.</li>
</ul>

<h2>For Linux Users</h2>
<ul>
  <li>This uses <a href = "https://www.commandlinux.com/man-page/man1/xrandr.1.html">xrandr</a> for brightness control.</li>
  <li>To install xrandr:</li>
  <ul>
    <li>Debian/Ubuntu: <code>sudo apt install x11-xserver-utils</code>.</li>
    <li>Fedora: <code>sudo dnf install libXrandr</code>.</li>
    <li>Arch: <code>sudo pacman -S xorg-xrandr</code>.</li>
  </ul>
</ul>
<h2>For MacOS Users</h2>
<ul>
  <li>This uses <a href = "https://github.com/nriley/brightness">brightness</a> for brightness control.</li>
  <li>To install brightness:</li>
  <code>git clone https://github.com/nriley/brightness.git && cd brightness && make && sudo make install</code>

</ul>

