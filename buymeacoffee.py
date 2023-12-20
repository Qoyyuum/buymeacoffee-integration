from pydantic import BaseModel, EmailStr
from typing import Optional

class Extras(BaseModel):
    """
     {
        id: 3,
        title: "Content Creation Advice",
        amount: "75.00",
        object: "extra",
        currency: "USD",
        description: "Hop on a Zoom call with me where I’ll spend an hour to help you achieveyour content creation goals. I’ll also show you the tools I use.",
        extra_question: "Would you like me to prepare before thecall? Feel free to leave any information here. ",
        "question_answers": []
     }
     """
    id: int
    title: str
    amount: str
    object: str
    currency: str
    description: str
    extra_question: str
    question_answers: list[str]

class PurchaseData(BaseModel):
    """
      id: 59,
      amount: 75,
      extras: [
      ],
      object: "payment",
      status: "succeeded",
      message: "John just claimed Content Creation Advice",
      currency: "USD",
      refunded: "false",
      created_at: 1676545577,
      note_hidden: "false",
      refunded_at: null,
      support_note: null,
      support_type: "Extra",
      supporter_name: "John",
      transaction_id: "pi_3Mc5I3JEtINljGAa0XZxB3XG",
      application_fee: "3.75",
      supporter_id: 2345,
      supporter_email: "john@example.com",
      total_amount_charged: "77.48"
   }
   """
    id: int
    amount: int
    extras: list[Extras]
    object: str
    status: str
    message: str
    currency: str
    refunded: str
    created_at: int
    note_hidden: str
    refunded_at: Optional[str] = None
    support_note: Optional[str] = None
    support_type: str
    supporter_name: str
    transaction_id: str
    application_fee: str
    supporter_id: int
    supporter_email: EmailStr
    total_amount_charged: str


class Purchase(BaseModel):
    """
    {
       type: "extra_purchase.created",
       live_mode: false,
       attempt: 1,
       created: 1703056736,
       event_id: 1,
       data: 
    }
    """
    type: str
    live_mode: bool
    attempt: int
    created: int
    event_id: int
    data: PurchaseData 

