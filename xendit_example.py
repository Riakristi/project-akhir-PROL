import xendit
from xendit import EWallet
import qrcode, json
xendit.api_key = "xnd_development_nQN91JP7PtSKjWmf9dJJRpltxiS3nF0gXRvsFsdGMF7b92VxlAy7doG1pV2tMO"

def create_charge(harga, quantity):
    basket = []
    basket_item = EWallet.helper_create_basket_item(
        reference_id = "basket-product-ref-id",
        name = "product_name",
        category = "product_category",
        currency = "IDR",
        price = harga,
        quantity = quantity,
        type = "product_type",
        sub_category = "product_sub_category",
        metadata = {
            "meta": "data"
        }
    )
    basket.append(basket_item)

    ewallet_charge = EWallet.create_ewallet_charge(
        reference_id="basket-product-ref-id",
        currency="IDR",
        amount=harga*quantity,
        checkout_method="ONE_TIME_PAYMENT",
        channel_code="ID_SHOPEEPAY",
        channel_properties={
            "success_redirect_url": "https://yourwebsite.com/order/123",
        },
        basket=basket,
    )
    
    qr_string = ewallet_charge.actions['mobile_deeplink_checkout_url']
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_string)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('test.png')
    
    return ewallet_charge

def check_status(charge_id):
    ewallet_status = EWallet.get_ewallet_charge_status(
        charge_id=charge_id,
    )
    return ewallet_status

if __name__ == '__main__':
    request = create_charge(5000, 2)
    charge_id = request.id
    enter = int(input("Bayar? 0/1: "))
    while enter == 0:
        enter = int(input("Bayar? 0/1: "))
    status = check_status(charge_id)
    print(status.status)


    


