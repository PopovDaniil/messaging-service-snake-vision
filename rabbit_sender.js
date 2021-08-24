import amqp from 'amqp'

const conn = amqp.createConnection({ host: 'localhost' })

conn.on('ready', function () {     
    conn.publish('control', 'hello')
    conn.destroy()
  });