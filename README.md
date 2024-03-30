<h1>Content Aware Auto Brightness</h1>
<p>
  A simple Python script to change brightness based on the content on your screen.
</p>
<p>
  Currently for Windows only.(Testing MacOS and Linux)
</p>

<h2>To Install</h2>
<ul>
  <li>Clone this repository.</li>
  <li>Run <code>pip install -r setup.txt</code>.</li>
  <li>Run <code>python main.py</code>.</li>
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
