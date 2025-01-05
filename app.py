from nicegui import ui

@ui.page('/')
async def main():
    counter = 0  # This variable is now unique for each client

    def increment():
        nonlocal counter
        counter += 1
        label.text = f'Counter: {counter}'
        ui.notify('Clicked',position='center')

    label = ui.label(f'Counter: {counter}')
    ui.button('Increment', on_click=increment)

ui.run()
