import amqp from 'amqp'

const conn = amqp.createConnection({ host: 'localhost' })

conn.on('ready', function () {
    conn.queue('', function (q) {
        q.bind('#', 'control');
        
        q.subscribe(function (message) {
            console.log(message);
        });
    });
  });