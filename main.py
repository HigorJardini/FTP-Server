from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal   import Portal
from twisted.internet      import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm

#For add user on linux
checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("higor",    "12345")
checker.addUser("someuser", "12345")

#Public folder and private folders from users
portal = Portal(FTPRealm("./public", "./private"), [AllowAnonymousAccess(), checker])

factory = FTPFactory(portal)

#2121 is FTPFactory Port
reactor.listenTCP(2121, factory)
reactor.run()