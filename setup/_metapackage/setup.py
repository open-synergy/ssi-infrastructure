import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-infrastructure",
    description="Meta package for open-synergy-ssi-infrastructure Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_infrastructure',
        'odoo14-addon-ssi_infrastructure_server',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
