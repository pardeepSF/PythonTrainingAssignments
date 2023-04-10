import click

@click.command()

@click.option('--name','-n',default='Pardeep',help='Firstname description')


@click.option('--topic','-s',help='Tutorial name')


@click.option('--location','-l',help="work from home location",multiple=True)

def main(name,topic,location):
	click.echo('Hello World My Name is {},My Topic is {}'.format(name,topic))
	click.echo('\n'.join(location))



if __name__ == '__main__':
	main()
