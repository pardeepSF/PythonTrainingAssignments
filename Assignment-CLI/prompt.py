import click

@click.command()
@click.option('--name', default ='kumar')
@click.option('--password',prompt=True,hide_input=True,confirmation_prompt=True)

def main(name,password):
	fname = click.prompt("Enter Your Firstname")
	click.echo(f"Your Name is {name} and your firstname is {fname} your password is {password} ")

if __name__ == '__main__':
	main()