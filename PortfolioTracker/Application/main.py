from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class DividendPaymentModel(db.Model):
    id =  db.Column( db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), nullable = False)
    payment = db.Column(db.Float, nullable = False)
    date = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return f"DivdendPayment(ticker={ticker}, payment={payment}, date={date})"


dividend_payment_put_args = reqparse.RequestParser()
dividend_payment_put_args.add_argument("ticker", type=str,help="Missing Ticker Symbol", required=True)
dividend_payment_put_args.add_argument("payment", type=float,help="Missing Payment Ammount ", required=True)
dividend_payment_put_args.add_argument("date", type=str,help="Missing Date", required=True)

resource_fields ={
    'id': fields.Integer,
    'ticker': fields.String,
    'payment': fields.Float,
    'date': fields.String
}

class DividendPayment(Resource):

    @marshal_with(resource_fields)
    def get(self, id):
        result = DividendPaymentModel.query.filter_by(id = id).first()
        return result

    @marshal_with(resource_fields)
    def put(self,id):
        args = dividend_payment_put_args.parse_args()
        result = DividendPaymentModel.query.filter_by(id = id).first()
        if result:
            abort(409, message="id taken...")
             
        dividendPayment = DividendPaymentModel(id = id, ticker = args['ticker'], payment = args['payment'], date = args['date'])
        db.session.add(dividendPayment)
        db.session.commit()
        return dividendPayment, 201

api.add_resource(DividendPayment, "/dividendPayment/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)


       