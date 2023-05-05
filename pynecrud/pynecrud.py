import pynecone as pc
from .mymodel.food import Foods



class State(pc.State):
    name:str
    price:int
    stock:int
    columns = ["Name", "Age", "Location"]

    data = [
            ("Tolol", 30, "New York"),
            ("Tolol", 25, "San Francisco"),
        ]
    def showme(self,row):
        print("tolol",row)

    def addnew(self):
        if self.name and self.price and self.stock:
            try:
                with pc.session() as s:
                    s.add(
                        Foods(
                            food_name=self.name,
                            price=self.price,
                            stock=self.stock
                            )
                        )
                    s.commit()
            except Exception as e:
                print(e)
        else:
            print("Please fill in all fields before adding new food.")



def index():
    return pc.vstack(
        pc.heading("Crud Pynecone",size="md"),
        pc.input(
            focus_border_color="purple",
            placeholder="Food Name",
            on_change=State.set_name),

        pc.input(
            focus_border_color="purple",
            placeholder="Price",
            on_change=State.set_price),
        pc.input(
            focus_border_color="purple",
            placeholder="Stock",
            on_change=State.set_stock),


        pc.button("addnew",
            bg="yellow",color="black",size="lg",
        on_click=State.addnew
            ),

        # SHOW DATA IN TABLE
        pc.table_container(
            pc.table(
                pc.table_caption("Example Table"),
                pc.thead(
                    pc.tr(*[pc.th(column) for column in State.columns])
                ),
                # pc.tbody(
                #     *[
                #         pc.tr(*[pc.td(item) for item in row])
                #         for row in State.data
                #     ]
                # ),
                # pc.tfoot(pc.tr(*[pc.th(item) for item in footer])),
            )
        )
        )



# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
