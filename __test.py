import util_mysql as sql

session = sql.openSession()
sql.insCS(session,'test',1,20240201,1,1,1,1,1,1,1,1)
sql.closeSession(session)