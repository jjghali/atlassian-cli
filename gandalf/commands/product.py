import click

@click.group()
@click.option('-n', '--product-name', default=False)
@click.pass_context
def product(ctx,product_name):
    context_parent = click.get_current_context()    
    ctx.ensure_object(dict)    
    
    ctx.obj['PRODUCT_NAME'] = product_name
    ctx.obj['ATLASSIAN_USERNAME'] = context_parent.obj['ATLASSIAN_USERNAME']
    ctx.obj['ATLASSIAN_PASSWORD'] = context_parent.obj['ATLASSIAN_PASSWORD']

@product.command()
def list():
    """Lists all the deployed versions of a product"""        
    print("lists products")
    
@product.command()
@click.pass_context
def versions(ctx):
    """Lists all the deployed versions of a product"""    
    productName = ctx.obj["PRODUCT_NAME"]
    print("lists product versions")
    print(productName)
    context_parent = click.get_current_context()    

@product.command()
@click.pass_context
def components(ctx):
    """Lists all components of a product"""        
    productName = ctx.obj["PRODUCT_NAME"]
    print("lists products components")
    print(productName)
