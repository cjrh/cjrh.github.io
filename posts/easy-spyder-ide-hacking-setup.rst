.. link: 
.. description: 
.. tags: 
.. date: 2012/12/20 17:32:00
.. title: Easy Spyder IDE hacking setup
.. slug: easy-spyder-ide-hacking-setup

I am using pythonxy. I quite like the Spyder IDE that is provided with the
distro. If you want to set things up so that you can easily hack on Spyder
while keeping your python path setup sane, it is quite easy:

#. Delete `\site-packages\spyderlib`  
#. Delete `\site-packages\spyderplugins` 
#. Create `\site-packages\spyderlib.pth` with contents: 
   `D:\path\to\spyderlib\hg\repo`

This setup makes it easy to hack on Spyder, bugfixes, enhancements,
etc. and pull new versions of spyder while still working easily from your main
python (e.g. pythonxy) distro.

