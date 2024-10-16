from django import forms
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    EmailField,
    ImageField,
    IntegerField,
    TextField,
)


class BasicFactsheet(models.Model):
    model_name = CharField(
        max_length=1000,
        verbose_name="Name",
        help_text="What is the full model name?",
        null=False,
        unique=True,
    )
    acronym = CharField(
        max_length=20,
        verbose_name="Acronym",
        help_text="What is the abbreviation?",
        null=True,
    )
    institutions = ArrayField(
        CharField(max_length=1000),
        help_text="Which institutions develop(ed) the model?",
        default=list,
        null=True,
        verbose_name="Institution(s)",
    )
    authors = ArrayField(
        CharField(max_length=300),
        help_text="Who are the authors? Where do / did they work, on which parts of the model, during which time period?",  # noqa
        default=list,
        null=True,
        verbose_name="Author(s) (institution, working field, active time period)",
    )
    current_contact_person = CharField(
        max_length=1000,
        verbose_name="Current contact person",
        help_text="Who is the main contact person?",
        null=True,
    )
    contact_email = ArrayField(
        EmailField(),
        verbose_name="Contact (e-mail)",
        help_text="Please provide the mailadress of the contact person.",
        null=False,
    )
    contact_phone = CharField(
        max_length=200,
        verbose_name="Phone",
        help_text="WWhat is the website of the framework? Please provide a link!",
        null=True,
    )
    website = CharField(
        max_length=200,
        verbose_name="Website",
        help_text="If a website for the model exists please put the link here",
        null=True,
    )
    logo = ImageField(
        upload_to="logos",
        verbose_name="Logo",
        help_text="If a logo for the model exists load it up",
        null=True,
    )
    primary_purpose = TextField(
        verbose_name="Primary Purpose",
        help_text="What is the primary purpose of the model?",
        null=True,
    )
    primary_outputs = TextField(
        verbose_name="Primary Outputs",
        help_text="What are the main outputs of the model?",
        null=True,
    )
    support = BooleanField(
        default=False,
        verbose_name="Support / Community / Forum",
        help_text="What kind of support is available? Please check the boxes!",
    )

    framework = BooleanField(
        default=False,
        verbose_name="Framework",
        help_text="Is the model based on a framework? If yes, which?",
    )
    framework_yes_text = CharField(max_length=1000, null=True)

    user_documentation = CharField(
        max_length=500,
        verbose_name="Link to User Documentation",
        help_text="Is an user documentation available for the framework? Please insert the link",  # noqa
        null=True,
    )

    code_documentation = CharField(
        max_length=200,
        verbose_name="Link to Developer/Code Documentation",
        help_text="If a code documentation and or a developer documentation is publicly available please insert the link",  # noqa
        null=True,
    )
    documentation_quality = CharField(
        max_length=1000,
        verbose_name="Documentation quality",
        help_text="How do you rate the quality of the documentations?",
        choices=(
            (x, x) for x in ["not available", "expandable", "good", "excellent"]
        ),  # noqa
        default="expandable",
        null=True,
    )
    source_of_funding = CharField(
        max_length=200,
        verbose_name="Source of funding",
        help_text="What is the main source of funding for the development of the model?",  # noqa
        null=True,
    )
    open_source = BooleanField(
        default=False,
        verbose_name="Open Source",
        help_text="Is the framework published under an open source license?",
    )
    open_up = BooleanField(
        default=False,
        verbose_name="Planned to open up in the future",
        help_text="Will the source code be available in future?",
    )
    costs = CharField(max_length=1000, verbose_name="Costs", null=True)
    license = CharField(
        max_length=50,
        verbose_name="License",
        help_text="Under which license is the framework published?",
        choices=(
            (x, x)
            for x in [
                "Academic Free License v3.0",
                "Apache license 2.0",
                "Artistic license 2.0",
                "Boost Software License 1.0",
                'BSD 2-clause "Simplified" license',
                "BSD 3-clause Clear license",
                "Creative Commons license family",
                "Creative Commons Zero v1.0 Universal",
                "Creative Commons Attribution 4.0",
                "Creative Commons Attribution Share Alike 4.0",
                "Do What The F*ck You Want To Public License",
                "Educational Community License v2.0",
                "Eclipse Public License 1.0",
                "European Union Public License 1.1",
                "GNU Affero General Public License v3.0",
                "GNU General Public License family",
                "GNU General Public License v2.0",
                "GNU General Public License v3.0",
                "GNU Lesser General Public License family",
                "GNU Lesser General Public License v2.1",
                "GNU Lesser General Public License v3.0",
                "ISC",
                "LaTeX Project Public License v1.3c",
                "Microsoft Public License",
                "MIT",
                "Mozilla Public License 2.0",
                "Open Software License 3.0",
                "PostgreSQL License",
                "SIL Open Font License 1.1",
                "University of Illinois/NCSA Open Source License",
                "The Unlicense",
                "zLib License",
                "BSD 3-clause 'New' or 'Revised' license",
                "Other",
                "Unknown",
            ]
        ),
        default="Unknown",
    )
    license_other_text = CharField(max_length=1000, null=True)
    source_code_available = BooleanField(
        default=False,
        verbose_name="Source code available",
        help_text="Is the source code directly downloadable?",
    )
    gitHub = BooleanField(
        default=False,
        verbose_name="GitHub",
        help_text="Is the model available on GitHub?",
    )
    link_to_source_code = CharField(
        max_length=200,
        verbose_name="Access to source code",
        help_text="Is the source code to install and run a model available? If possible please provide a link to GitHub e.g. 'https://github.com/OpenEnergyPlatform/oeplatform'. You are free to provide a link to other sources then GitHub.",  # noqa
        null=True,
    )
    data_provided = CharField(
        max_length=1000,
        verbose_name="Data provided",
        help_text="Is the necessary data to run a scenario available?",
        choices=(
            ("none", "none"),
            ("example data", "example data"),
            ("all data", "all data"),
        ),
        default="none",
    )
    cooperative_programming = BooleanField(
        default=False,
        verbose_name="Collaborative programming",
        help_text="Is it possible to join the coding group?",
    )
    number_of_devolopers = CharField(
        max_length=1000,
        verbose_name="Number of developers",
        help_text="How many people are involved in the model development?",
        choices=(
            ("less than 10", "less than 10"),
            (" less than 20", " less than 20"),
            (" less than 50", " less than 50"),
            (" more than 50", " more than 50"),
        ),
        null=True,
    )
    number_of_users = CharField(
        max_length=1000,
        verbose_name="Number of users ",
        help_text="How many people approximately use the model?",
        choices=(
            ("less than 10", "less than 10"),
            (" less than 100", " less than 100"),
            (" less than 1000", " less than 1000"),
            (" more than 1000", " more than 1000"),
        ),
        null=True,
    )
    modelling_software = ArrayField(
        models.CharField(max_length=1000),
        help_text="Which modelling software and which version is used?",
        verbose_name="Modelling software ",
        default=list,
        null=True,
    )
    interal_data_processing_software = ArrayField(
        models.CharField(max_length=1000),
        help_text="Which data processing software is required? Please list all software (packages) that are used for internal data processing",  # noqa
        verbose_name="Internal data processing software",
        default=list,
        null=True,
    )
    # TODO: external_optimizer is not used anymore since the form adds a array element,
    # a boolean field is not needed anymore
    external_optimizer = BooleanField(
        default=False,
        verbose_name="External optimizer",
        help_text="Which external optimizer(s) can the model apply (e.g. Pyomo)? Please list them.",  # noqa
        null=False,
    )
    external_optimizer_yes_text = ArrayField(
        models.CharField(max_length=1000),
        verbose_name="External optimizer",
        help_text="Which external optimizer(s) can the model apply (e.g. Pyomo)? Please list them.",  # noqa
        default=list,
        null=True,
    )

    additional_software = ArrayField(
        models.CharField(max_length=1000),
        help_text="Which additional software is required to run the model?",
        verbose_name="Additional software",
        default=list,
        null=True,
    )
    gui = BooleanField(
        default=False,
        verbose_name="GUI",
        help_text="Is a graphical user interface available?",
        null=False,
    )

    citation_reference = CharField(
        max_length=10000,
        verbose_name="Citation reference",
        help_text="Are publications available about the framework? Please list!",  # noqa
        null=True,
    )
    citation_DOI = CharField(
        max_length=10000,
        verbose_name="Citation DOI",
        help_text="If  there are publications about the model that have a DOI please list the DOIs",  # noqa
        null=True,
    )
    references_to_reports_produced_using_the_model = CharField(
        max_length=10000,
        verbose_name="Reference Studies/Models",
        help_text="Which studies were calculated/ Which models were developed  with the framework?",  # noqa
        null=True,
    )
    larger_scale_usage = CharField(
        max_length=10000,
        verbose_name="Model usage",
        help_text="Is this model used from various (maybe well known) institutions? If so, who uses it?",  # noqa
        null=True,
    )

    tags = ArrayField(IntegerField(), default=list, null=True)


class Energymodel(BasicFactsheet):
    energy_sectors_electricity = BooleanField(
        default=False, verbose_name="electricity"
    )  # noqa
    energy_sectors_heat = BooleanField(default=False, verbose_name="heat")
    energy_sectors_liquid_fuels = BooleanField(
        default=False, verbose_name="liquid fuels"
    )
    energy_sectors_gas = BooleanField(default=False, verbose_name="gas")
    energy_sectors_others = BooleanField(default=False, verbose_name="others")
    energy_sectors_others_text = CharField(max_length=200, null=True)

    def energy_sectors(self):
        return [
            self.energy_sectors_electricity,
            self.energy_sectors_heat,
            self.energy_sectors_liquid_fuels,
            self.energy_sectors_gas,
        ]

    methodical_focus_1 = CharField(
        max_length=50,
        verbose_name="Methodical Focus",
        help_text='1-3 Keyords describing the main methodical focus of the model e.g."open source", "sector coupling"',  # noqa
        null=True,
    )
    methodical_focus_2 = CharField(max_length=50, null=True, blank=True)
    methodical_focus_3 = CharField(max_length=50, null=True, blank=True)

    demand_sectors_households = BooleanField(
        default=False, verbose_name="Households"
    )  # noqa
    demand_sectors_industry = BooleanField(
        default=False, verbose_name="Industry"
    )  # noqa
    demand_sectors_commercial_sector = BooleanField(
        default=False, verbose_name="Commercial sector"
    )
    demand_sectors_transport = BooleanField(
        default=False, verbose_name="Transport"
    )  # noqa

    energy_carrier_gas_natural_gas = BooleanField(
        default=False, verbose_name="Natural gas"
    )
    energy_carrier_gas_biogas = BooleanField(
        default=False, verbose_name="Biogas"
    )  # noqa
    energy_carrier_gas_hydrogen = BooleanField(
        default=False, verbose_name="Hydrogen"
    )  # noqa

    energy_carrier_liquids_petrol = BooleanField(
        default=False, verbose_name="Petrol"
    )  # noqa
    energy_carrier_liquids_diesel = BooleanField(
        default=False, verbose_name="Diesel"
    )  # noqa
    energy_carrier_liquids_ethanol = BooleanField(
        default=False, verbose_name="Ethanol"
    )  # noqa

    energy_carrier_solid_hard_coal = BooleanField(
        default=False, verbose_name="Hard coal"
    )
    energy_carrier_solid_hard_lignite = BooleanField(
        default=False, verbose_name="Lignite"
    )
    energy_carrier_solid_hard_uranium = BooleanField(
        default=False, verbose_name="Uranium"
    )
    energy_carrier_solid_hard_biomass = BooleanField(
        default=False, verbose_name="Biomass"
    )

    energy_carrier_renewables_sun = BooleanField(
        default=False, verbose_name="Sun"
    )  # noqa
    energy_carrier_renewables_wind = BooleanField(
        default=False, verbose_name="Wind"
    )  # noqa
    energy_carrier_renewables_hydro = BooleanField(
        default=False, verbose_name="Hydro"
    )  # noqa
    energy_carrier_renewables_geothermal_heat = BooleanField(
        default=False, verbose_name="Geothermal heat"
    )

    generation_renewables_PV = BooleanField(default=False, verbose_name="PV")
    generation_renewables_wind = BooleanField(
        default=False, verbose_name="Wind"
    )  # noqa
    generation_renewables_hydro = BooleanField(
        default=False, verbose_name="Hydro"
    )  # noqa
    generation_renewables_biomass = BooleanField(
        default=False, verbose_name="Biomass"
    )  # noqa
    generation_renewables_biogas = BooleanField(
        default=False, verbose_name="Biogas"
    )  # noqa
    generation_renewables_bio = BooleanField(
        default=False, verbose_name="Biomass,Biogas,Biofuels"
    )
    generation_renewables_solar_thermal = BooleanField(
        default=False, verbose_name="Solar thermal"
    )
    generation_renewables_geothermal = BooleanField(
        default=False, verbose_name="Geothermal heat"
    )
    generation_renewables_others = BooleanField(
        default=False, verbose_name="Others"
    )  # noqa
    generation_renewables_others_text = CharField(max_length=200, null=True)

    generation_conventional_gas = BooleanField(
        default=False, verbose_name="gas"
    )  # noqa
    generation_conventional_coal = BooleanField(
        default=False, verbose_name="coal"
    )  # noqa
    generation_conventional_lignite = BooleanField(
        default=False, verbose_name="lignite"
    )
    generation_conventional_hard_coal = BooleanField(
        default=False, verbose_name="hard coal"
    )
    generation_conventional_oil = BooleanField(
        default=False, verbose_name="oil"
    )  # noqa
    generation_conventional_liquid_fuels = BooleanField(
        default=False, verbose_name="liquid fuels"
    )
    generation_conventional_nuclear = BooleanField(
        default=False, verbose_name="nuclear"
    )

    generation_CHP = BooleanField(default=False, verbose_name="CHP")

    modeled_technology_renewables = BooleanField(
        default=False, verbose_name="renewables"
    )
    modeled_technology_conventional = BooleanField(
        default=False, verbose_name="conventional"
    )

    transfer_electricity = BooleanField(
        default=False, verbose_name="electricity"
    )  # noqa
    transfer_electricity_distribution = BooleanField(
        default=False, verbose_name="distribution"
    )
    transfer_electricity_transition = BooleanField(
        default=False, verbose_name="transmission"
    )

    transfer_gas = BooleanField(default=False, verbose_name="gas")
    transfer_gas_distribution = BooleanField(
        default=False, verbose_name="distribution"
    )  # noqa
    transfer_gas_transition = BooleanField(
        default=False, verbose_name="transmission"
    )  # noqa

    transfer_heat = BooleanField(default=False, verbose_name="heat")
    transfer_heat_distribution = BooleanField(
        default=False, verbose_name="distribution"
    )
    transfer_heat_transition = BooleanField(
        default=False, verbose_name="transmission"
    )  # noqa

    network_coverage_AC = BooleanField(
        default=False, verbose_name="AC load flow"
    )  # noqa
    network_coverage_DC = BooleanField(
        default=False, verbose_name="DC load flow"
    )  # noqa
    network_coverage_TM = BooleanField(
        default=False, verbose_name="transshipment model"
    )
    network_coverage_SN = BooleanField(
        default=False, verbose_name="single-node / copper plate model"
    )
    network_coverage_other = BooleanField(default=False, verbose_name="other")
    network_coverage_other_text = CharField(max_length=200, null=True)

    storage_electricity_battery = BooleanField(
        default=False, verbose_name="battery"
    )  # noqa
    storage_electricity_kinetic = BooleanField(
        default=False, verbose_name="kinetic"
    )  # noqa
    storage_electricity_CAES = BooleanField(
        default=False, verbose_name="compressed air"
    )
    storage_electricity_PHS = BooleanField(
        default=False, verbose_name="pump hydro"
    )  # noqa
    storage_electricity_chemical = BooleanField(
        default=False, verbose_name="chemical"
    )  # noqa

    storage_heat = BooleanField(default=False, verbose_name="heat")
    storage_gas = BooleanField(default=False, verbose_name="gas")

    user_behaviour = BooleanField(
        default=False,
        verbose_name="User behaviour and demand side management",
        help_text="Can user behaviour and demand side management be considered in the model? If yes please shortly explain how that is realised.",  # noqa
    )
    user_behaviour_yes_text = TextField(null=True)
    changes_in_efficiency = TextField(
        null=True,
        verbose_name="Changes in efficiency",
        help_text="Can changes in efficiency be considered in the model? If yes please shortly explain how that is realised.",  # noqa
    )

    market_models = CharField(
        max_length=20,
        verbose_name="Market models",
        choices=((x, x) for x in ["fundamental model", "stochastic model"]),
        null=True,
        help_text="If the described model is not a market model itself please indicate if a market model is included - if yes,  which one?",  # noqa
    )

    geographical_coverage = ArrayField(
        models.CharField(max_length=1000),
        help_text="What regions are covered? Please, list the regions covered by the model. Leave blank, if the model and data are not limited to a specific region. Example input: USA, Canada, Mexico",  # noqa
        verbose_name="Geographical coverage",
        default=list,
        null=True,
    )

    geo_resolution_global = BooleanField(default=False, verbose_name="global")
    geo_resolution_continents = BooleanField(
        default=False, verbose_name="continents"
    )  # noqa
    geo_resolution_national_states = BooleanField(
        default=False, verbose_name="national states"
    )
    geo_resolution_TSO_regions = BooleanField(
        default=False, verbose_name="TSO regions"
    )  # noqa
    geo_resolution_federal_states = BooleanField(
        default=False, verbose_name="federal states"
    )
    geo_resolution_regions = BooleanField(default=False, verbose_name="regions")  # noqa
    geo_resolution_NUTS_3 = BooleanField(default=False, verbose_name="NUTS 3")
    geo_resolution_municipalities = BooleanField(
        default=False, verbose_name="municipalities"
    )
    geo_resolution_districts = BooleanField(
        default=False, verbose_name="districts"
    )  # noqa
    geo_resolution_households = BooleanField(
        default=False, verbose_name="households"
    )  # noqa
    geo_resolution_power_stations = BooleanField(
        default=False, verbose_name="power stations"
    )
    geo_resolution_others = BooleanField(default=False, verbose_name="others")
    geo_resolution_others_text = CharField(max_length=200, null=True)

    comment_on_geo_resolution = TextField(
        verbose_name="Comment on geographic (spatial) resolution",
        help_text="Feel free to explain the geographical resolution of the model e.g. with regard to the grid data.",  # noqa
        null=True,
    )

    @property
    def time_resolution(self):
        return [
            self.time_resolution_1_min,
            self.time_resolution_15_min,
            self.time_resolution_hour,
            self.time_resolution_anual,
        ]

    time_resolution_anual = BooleanField(default=False, verbose_name="annual")
    time_resolution_hour = BooleanField(default=False, verbose_name="hour")
    time_resolution_15_min = BooleanField(default=False, verbose_name="15 min")
    time_resolution_1_min = BooleanField(default=False, verbose_name="1 min")

    observation_period_more_1_year = BooleanField(
        default=False, verbose_name=">1 year"
    )  # noqa
    observation_period_less_1_year = BooleanField(
        default=False, verbose_name="<1 year"
    )  # noqa
    observation_period_1_year = BooleanField(
        default=False, verbose_name="1 year"
    )  # noqa
    observation_period_other = BooleanField(default=False, verbose_name="other")  # noqa
    observation_period_other_text = CharField(max_length=200, null=True)

    time_resolution_other = BooleanField(default=False, verbose_name="other")
    time_resolution_other_text = CharField(max_length=200, null=True)

    additional_dimensions_sector_ecological = BooleanField(
        default=False, verbose_name="ecological"
    )
    additional_dimensions_sector_ecological_text = CharField(
        max_length=1000, null=True
    )  # noqa
    additional_dimensions_sector_economic = BooleanField(
        default=False, verbose_name="economic"
    )
    additional_dimensions_sector_economic_text = CharField(
        max_length=1000, null=True
    )  # noqa
    additional_dimensions_sector_social = BooleanField(
        default=False, verbose_name="social"
    )
    additional_dimensions_sector_social_text = CharField(
        max_length=1000, null=True
    )  # noqa
    additional_dimensions_sector_others = BooleanField(
        default=False, verbose_name="others"
    )
    additional_dimensions_sector_others_text = CharField(
        max_length=1000, null=True
    )  # noqa

    model_class_optimization_LP = BooleanField(default=False, verbose_name="LP")  # noqa
    model_class_optimization_MILP = BooleanField(
        default=False, verbose_name="MILP"
    )  # noqa
    model_class_optimization_Nonlinear = BooleanField(
        default=False, verbose_name="Nonlinear"
    )
    model_class_optimization_LP_MILP_Nonlinear_text = CharField(
        max_length=1000, null=True
    )

    model_class_simulation_Agentbased = BooleanField(
        default=False, verbose_name="Agent-based"
    )
    model_class_simulation_System_Dynamics = BooleanField(
        default=False, verbose_name="System Dynamics"
    )
    model_class_simulation_Accounting_Framework = BooleanField(
        default=False, verbose_name="Accounting Framework"
    )
    model_class_simulation_Game_Theoretic_Model = BooleanField(
        default=False, verbose_name="Game Theoretic Model"
    )
    model_class_simulation_bottom_up = BooleanField(
        default=False, verbose_name="Bottom up"
    )
    model_class_simulation_top_down = BooleanField(
        default=False, verbose_name="Top down"
    )

    model_class_other = BooleanField(default=False, verbose_name="Other")
    model_class_other_text = CharField(max_length=1000, null=True)

    short_description_of_mathematical_model_class = TextField(
        verbose_name="Short description of mathematical model class",
        help_text="Here you can explain little more the model class in your own words if you think that the above categorisation is not explicative enough.",  # noqa
        null=True,
    )

    mathematical_objective_cO2 = BooleanField(default=False, verbose_name="CO2")  # noqa
    mathematical_objective_costs = BooleanField(
        default=False, verbose_name="costs"
    )  # noqa
    mathematical_objective_rEshare = BooleanField(
        default=False, verbose_name="RE-share"
    )
    mathematical_objective_other = BooleanField(
        default=False, verbose_name="other"
    )  # noqa
    mathematical_objective_other_text = CharField(max_length=200, null=True)

    uncertainty_deterministic = BooleanField(
        default=False, verbose_name="Deterministic"
    )
    uncertainty_Stochastic = BooleanField(
        default=False, verbose_name="Stochastic"
    )  # noqa
    uncertainty_Other = BooleanField(default=False, verbose_name="Other")
    uncertainty_Other_text = CharField(
        max_length=200, null=True, verbose_name="Other"
    )  # noqa

    montecarlo = BooleanField(
        default=False, verbose_name="Suited for many scenarios / monte-carlo"
    )

    typical_computation_time = CharField(
        max_length=30,
        choices=(
            (x, x)
            for x in [
                "less than a second",
                "less than a minute",
                "less than an hour",
                "less than a day",
                "more than a day",
            ]
        ),
        null=True,
    )

    typical_computation_hardware = CharField(
        max_length=10000,
        verbose_name="Typical computation hardware",
        help_text="Here you can specify which hardware was assumed to estimate above time (e.g. RAM, CPU, GPU, etc).",  # noqa
        null=True,
    )
    technical_data_anchored_in_the_model = CharField(
        max_length=10000,
        verbose_name="Technical data anchored in the model",
        help_text="If there is technical data already embedded (hard code) in the model and not part of the scenario, please make that transparent here.",  # noqa
        null=True,
    )

    validation_models = BooleanField(
        verbose_name="cross-checked with other models", default=False
    )
    validation_measurements = BooleanField(
        verbose_name="checked with measurements (measured data)", default=False
    )
    validation_others = BooleanField(verbose_name="others", default=False)
    validation_others_text = CharField(max_length=1000, null=True)

    model_specific_properties = CharField(
        max_length=10000,
        verbose_name="Model specific properties",
        help_text="What are main specific characteristics (strengths and weaknesses) of this model regarding the purpose of the recommendation?",  # noqa
        null=True,
    )
    example_research_questions = CharField(
        max_length=10000,
        verbose_name="Example research questions",
        help_text="Which would be good research questions that could be answered with the model?",  # noqa
        null=True,
    )
    properties_missed = TextField(
        verbose_name="further properties",
        help_text="Which properties of your model have not been mentioned on this factsheet? Please note them.",  # noqa
        null=True,
    )

    interfaces = TextField(
        verbose_name="Interfaces",
        help_text="Which APIs does the model have?",
        null=True,
    )
    model_file_format = CharField(
        max_length=5,
        choices=map(lambda x: (x, x), (".exe", ".gms", ".py", ".xls", "Other")),  # noqa
        verbose_name="Model file format",
        help_text="In which format is the model saved?",
        default="other",
        null=True,
    )
    model_file_format_other_text = CharField(max_length=1000, null=True)
    model_input = CharField(
        max_length=5,
        choices=map(lambda x: (x, x), (".csv", ".py", "text", ".xls", "Other")),  # noqa
        verbose_name="Input data file format",
        help_text="Of which file format are the input data?",
        default="other",
        null=True,
    )
    model_input_other_text = CharField(max_length=1000, null=True)
    model_output = CharField(
        max_length=5,
        choices=map(lambda x: (x, x), (".csv", ".py", "text", ".xls", "Other")),  # noqa
        verbose_name="Output data file format",
        help_text="Of which file format are the output data?",
        default="other",
        null=True,
    )
    model_output_other_text = CharField(max_length=1000, null=True)
    integrating_models = ArrayField(
        TextField(),
        verbose_name="Integration with other models",
        help_text="With which models has this model been integrated into (providing a link)? Where is the combined model available?",  # noqa
        null=True,
    )
    integrated_models = ArrayField(
        TextField(),
        verbose_name="Integration of other models",
        help_text="Which models are integrated in the model? Where are these models available?",  # noqa
        null=True,
    )

    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
        }
        defaults.update(kwargs)
        # Skip our parent's formfield implementation completely as we don't
        # care for it.
        # pylint:disable=bad-super-call
        return super(ArrayField, self).formfield(**defaults)


class Energyframework(BasicFactsheet):
    def __init__(self, *args, **kwargs):
        super(BasicFactsheet, self).__init__(*args, **kwargs)
        for o in self._meta.fields:
            if "help_text" in o.__dict__:
                o.help_text = o.help_text.replace("model", "framework")

    model_types_grid = BooleanField(
        default=False, verbose_name="Grid optimisation"
    )  # noqa
    model_types_demand_simulation = BooleanField(
        default=False, verbose_name="demand simulation"
    )
    model_types_feed_in_simulation = BooleanField(
        default=False, verbose_name="feed-in simulation"
    )
    model_types_other = BooleanField(default=False, verbose_name="Other")
    model_types_other_text = CharField(max_length=1000, null=True)

    api_doc = CharField(
        max_length=200, verbose_name="Link to API documentation", null=True
    )
    data_api = BooleanField(verbose_name="API to openmod database")
    abstraction = TextField(
        verbose_name="Points/degree of abstraction", null=True
    )  # noqa
    used = ArrayField(
        CharField(max_length=1000),
        verbose_name="Models using this framework",
        default=list,
        null=True,
    )
    inital_purpose = CharField(
        verbose_name="Inital purpose",
        null=True,
        help_text="What was the initial purpose/task/motivation to start the development?",  # noqa
        max_length=1000,
    )
    inital_purpose_change = CharField(
        verbose_name="Inital purpose change",
        null=True,
        help_text="Did that initial purpose change over time? If yes, what was the intentional purpose?",  # noqa
        max_length=1000,
    )
    inital_release_date = DateField(
        verbose_name="Inital Release Date",
        null=True,
        help_text="When [YYYY-MM-DD] was the framework initially released?",
        max_length=30,
    )
    research_questions = ArrayField(
        CharField(max_length=1000),
        verbose_name="Research questions",
        null=True,
        help_text="What are 3 typical research questions that are answered by applying the FW?",  # noqa
    )
    parent_framework = CharField(
        verbose_name="Parent Framework",
        null=True,
        help_text="Is the framework based on a framework? If yes, which?",
        max_length=80,
    )
    # GEOGRAPHICAL SCOPE
    gs_global = BooleanField(verbose_name="Global", default=False)
    gs_regional = BooleanField(verbose_name="Regional", default=False)
    gs_national = BooleanField(verbose_name="National", default=False)
    gs_local = BooleanField(verbose_name="Local/community", default=False)
    gs_single_project = BooleanField(
        verbose_name="Single-project", default=False
    )  # noqa
    gs_other = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )  # noqa
    # SECTORAL SCOPE
    ss_electricity = BooleanField(verbose_name="Electricity", default=False)
    ss_heat = BooleanField(verbose_name="Heat/Cooling", default=False)
    ss_transport = BooleanField(verbose_name="Transport", default=False)
    ss_other = BooleanField(
        verbose_name="Other specific sectors", default=False
    )  # noqa
    ss_overall = BooleanField(verbose_name="Overall economy", default=False)
    ss_other_text = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )
    # GENERAL PROBLEM SCOPE
    gps_forecast = BooleanField(verbose_name="Forecasting", default=False)
    gps_explore = BooleanField(verbose_name="Exploring", default=False)
    gps_backcast = BooleanField(verbose_name="Back casting", default=False)
    gps_other = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )  # noqa
    # SPECIFIC PROBLEM SCOPE
    sps_energydemand = BooleanField(verbose_name="Energy demand", default=False)  # noqa
    sps_energysupply = BooleanField(verbose_name="Energy supply", default=False)  # noqa
    sps_impacts = BooleanField(verbose_name="Impacts", default=False)
    sps_environmental = BooleanField(
        verbose_name="Environmental", default=False
    )  # noqa
    sps_appraisal = BooleanField(verbose_name="Appraisal", default=False)
    sps_integrated_approach = BooleanField(
        verbose_name="Integrated approach", default=False
    )
    sps_modular_buildup = BooleanField(
        verbose_name="Modular build-up", default=False
    )  # noqa
    sps_energy_dispatch = BooleanField(
        verbose_name="Energy dispatch", default=False
    )  # noqa
    sps_capacity_expansion = BooleanField(
        verbose_name="Capacity expansion planning", default=False
    )
    sps_unit_commitment = BooleanField(
        verbose_name="Unit commitment", default=False
    )  # noqa
    sps_rule_based = BooleanField(
        verbose_name="Rule based operation management", default=False
    )
    sps_sector_coupling = BooleanField(
        verbose_name="Sector-coupling ", default=False
    )  # noqa
    sps_other = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )  # noqa

    last_updated = DateField(
        verbose_name="Last updated",
        max_length=200,
        help_text="When was the factsheet last updated? Time format is [YYYY-MM-DD].",  # noqa
        null=True,
    )
    version = CharField(
        verbose_name="Version",
        max_length=200,
        help_text="To which version of the framework does the factsheet refer?",  # noqa
        null=True,
    )
    # PROGRAMMING FRAMEWORK
    pf_GAMS = BooleanField(verbose_name="GAMS", default=False)
    pf_Python = BooleanField(verbose_name="Python", default=False)
    pf_C = BooleanField(verbose_name="C++", default=False)
    pf_PHP = BooleanField(verbose_name="PHP", default=False)
    pf_GNU = BooleanField(verbose_name="GNU MathProg", default=False)
    pf_R = BooleanField(verbose_name="R", default=False)
    pf_VBA = BooleanField(verbose_name="MS Excel / VBA", default=False)
    pf_Java = BooleanField(verbose_name="Java", default=False)
    pf_Fortran = BooleanField(verbose_name="Fortran", default=False)
    pf_Modelica = BooleanField(verbose_name="Modelica", default=False)
    pf_Matlab = BooleanField(verbose_name="Matlab", default=False)
    pf_Ruby = BooleanField(verbose_name="Ruby", default=False)
    pf_other = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )  # noqa
    # EXTERNAL SOLVER
    es_CPLEX = BooleanField(verbose_name="CPLEX", default=False)
    es_Gurobi = BooleanField(verbose_name="Gurobi", default=False)
    es_Coin = BooleanField(verbose_name="Coin-Or CBC", default=False)
    es_GLPK = BooleanField(verbose_name="GLPK", default=False)
    es_MOSEK = BooleanField(verbose_name="MOSEK", default=False)
    es_other = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )  # noqa
    # INPUT DATA FORMAT
    idf_Pandas = BooleanField(
        verbose_name="Pandas DataFrame/Series", default=False
    )  # noqa
    idf_Python_dicts = BooleanField(verbose_name="Python dicts", default=False)
    idf_XLSX = BooleanField(verbose_name="XLSX", default=False)
    idf_Plots = BooleanField(verbose_name=" Plots (png, pdf)", default=False)
    idf_CSV = BooleanField(verbose_name="CSV", default=False)
    idf_XML = BooleanField(verbose_name="XML", default=False)
    idf_txt = BooleanField(verbose_name="txt", default=False)
    idf_db = BooleanField(verbose_name="db", default=False)
    idf_GAMS = BooleanField(
        verbose_name="GAMS data exchange format (gdx)", default=False
    )
    idf_other = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )  # noqa
    # OUTPUT DATA FORMAT
    odf_Pandas = BooleanField(
        verbose_name="Pandas DataFrame/Series", default=False
    )  # noqa
    odf_Python_dicts = BooleanField(verbose_name="Python dicts", default=False)
    odf_XLSX = BooleanField(verbose_name="XLSX", default=False)
    odf_Plots = BooleanField(verbose_name=" Plots (png, pdf)", default=False)
    odf_CSV = BooleanField(verbose_name="CSV", default=False)
    odf_XML = BooleanField(verbose_name="XML", default=False)
    odf_txt = BooleanField(verbose_name="txt", default=False)
    odf_db = BooleanField(verbose_name="db", default=False)
    odf_GAMS = BooleanField(
        verbose_name="GAMS data exchange format (gdx)", default=False
    )
    odf_other = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )  # noqa

    auto_model_generator = BooleanField(
        verbose_name="Auto model generator",
        help_text="Is an auto-Model generator available that transfers an input file into a Model?",  # noqa
        default=False,
    )
    data_preprocessing = BooleanField(
        verbose_name="data preprocessing",
        help_text="Are there any scripts for data pre-processing (e.g. calculating demand, economic functions) available",  # noqa
        default=False,
    )
    data_preprocessing_other = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )
    data_postprocessing = BooleanField(
        verbose_name="data postprocessing",
        help_text="Which output format(s) can the framework apply? Please list!",
        default=False,
    )
    data_postprocessing_other = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )
    plotting_functionalities = BooleanField(
        verbose_name="plotting functionalities",
        help_text="Are specific plotting functionalities available?",
        default=False,
    )
    # ANALYTICAL APPROACH
    ap_TopDown = BooleanField(verbose_name="Top Down", default=False)
    ap_BottomUp = BooleanField(verbose_name="Bottom up", default=False)
    ap_Hybrid = BooleanField(verbose_name="Hybrid", default=False)
    ap_Other = CharField(
        verbose_name="Other", max_length=400, help_text="", null=True
    )  # noqa

    interfaces = CharField(
        verbose_name="interfaces",
        max_length=200,
        help_text="Which interfaces to recommended, additional,  useful software is provided by the framework? Please list! ",  # noqa
        null=True,
    )

    # MATHEMATICAL APPROACH
    ma_lp = BooleanField(verbose_name="Linear Programming", default=False)
    ma_mip = BooleanField(verbose_name="Mixed integer programming", default=False)
    ma_dp = BooleanField(verbose_name="Dynamic Programming", default=False)
    ma_fl = BooleanField(verbose_name="Fuzzy Logic", default=False)
    ma_abp = BooleanField(verbose_name="Agent based programming", default=False)
    ma_other = CharField(verbose_name="Other", max_length=400, help_text="", null=True)
    # UNDERLYING METHODOLOGY
    um_econometric = BooleanField(verbose_name="Econometric", default=False)
    um_me = BooleanField(verbose_name="Macro-Economic", default=False)
    um_ee = BooleanField(verbose_name="Economic Equilibrium", default=False)
    um_optimization = BooleanField(verbose_name="Optimization", default=False)
    um_simulation = BooleanField(verbose_name="Simulation", default=False)
    um_stochastic = BooleanField(verbose_name="Stochastic/Monte-Carlo", default=False)
    um_gis = BooleanField(verbose_name="Spatial (GIS)", default=False)
    um_st = BooleanField(verbose_name="Spreadsheet/Toolbox", default=False)
    um_bc = BooleanField(verbose_name="Back casting", default=False)
    um_mc = BooleanField(verbose_name="Multi-Criteria", default=False)
    um_Accounting = BooleanField(verbose_name="Accounting", default=False)
    um_other = CharField(verbose_name="Other", max_length=400, help_text="", null=True)
    # OBJECTIVE FUNCTION TYPE
    oft_mtsc = BooleanField(verbose_name="Minimize Total System Cost", default=False)
    oft_mce = BooleanField(verbose_name="Minimize CO2-emissions", default=False)
    oft_mlce = BooleanField(
        verbose_name="Minimizing Levelized Cost of Energy", default=False
    )
    oft_msw = BooleanField(verbose_name="Maximize Social Welfare", default=False)
    oft_other = CharField(verbose_name="Other", max_length=400, help_text="", null=True)
    # SUPPORT
    support_forum = BooleanField(verbose_name="Forum", default=False)
    support_community = BooleanField(verbose_name="Community", default=False)
    support_workshop = BooleanField(verbose_name="Workshop", default=False)
    support_mail = BooleanField(verbose_name="Mail", default=False)
    support_modelExamples = BooleanField(verbose_name="Model Examples", default=False)
    support_other_text = CharField(verbose_name="Other", max_length=1000, null=True)

    link_to_code_documentation = CharField(
        verbose_name="Link to code documentation",
        max_length=200,
        help_text="Is a code/API documentation availaibe for the framework? Please insert the link!",  # noqa
        null=True,
    )
    skills_basic = CharField(
        verbose_name="Skills basic",
        max_length=200,
        help_text="What basic skills does a person need to become a user of the framework?",  # noqa
        null=True,
    )
    skills_advanced = CharField(
        verbose_name="Skills advanced",
        max_length=200,
        help_text="What advanced skills does a person need to become a user of the framework?",  # noqa
        null=True,
    )
    installation_guide = BooleanField(
        verbose_name="Installation guide",
        help_text="Is an installation guide provided for the framework (e.g. as part of the documentation)? Please provide a link",  # noqa
        default=False,
    )
    link_to_installation_guide = CharField(
        verbose_name="Link to installation guide",
        max_length=200,
        help_text="Is an installation guide availaibe for the framework? Please insert the link!",  # noqa
        null=True,
    )
    open_to_developers = BooleanField(
        verbose_name="Open to developers",
        help_text="Is it possible to join the developer group?",
        default=False,
    )

    source_code_availability = CharField(
        verbose_name="Code availability",
        max_length=200,
        help_text="What is the link to the source code?",
        null=True,
    )
    data_code_availability = CharField(
        verbose_name="Data availability",
        max_length=200,
        help_text="Is at least one (dummy) data set available to run a model built with the framework?",  # noqa
        null=True,
    )

    # RENEWABLE ENERGY INCLUSION
    Hydro = BooleanField(verbose_name="Hydro", default=False)
    Solar = BooleanField(verbose_name="Solar", default=False)
    Geothermal = BooleanField(verbose_name="Geothermal", default=False)
    Wind = BooleanField(verbose_name="Wind", default=False)
    Wave = BooleanField(verbose_name="Wave", default=False)
    Biomass = BooleanField(verbose_name="Biomass", default=False)
    Tidal = BooleanField(verbose_name="Tidal", default=False)
    # STORAGE TECHNOLOGY
    st_hydro = BooleanField(verbose_name="Pumped-hydro energy storage", default=False)
    st_battery = BooleanField(verbose_name="Battery energy storage", default=False)
    st_air = BooleanField(verbose_name="Compressed-air energy storage", default=False)
    st_hydrogen = BooleanField(
        verbose_name="Hydrogen production / storage / consumption", default=False
    )
    # DEMAND CHARACTERISTICS | TRANSPORT DEMAND
    dc_combustion = BooleanField(
        verbose_name="Internal-combustion vehicles", default=False
    )
    dc_battery = BooleanField(verbose_name="Battery-electric vehicles", default=False)
    dc_v2grid = BooleanField(
        verbose_name="Vehicle-to-grid electric vehicles", default=False
    )
    dc_hydrogen = BooleanField(verbose_name="Hydrogen vehicles", default=False)
    dc_rail = BooleanField(verbose_name="Rail", default=False)
    dc_aviation = BooleanField(verbose_name="Aviation", default=False)
    # DEMAND CHARACTERISTICS | RESIDENTAL DEMAND
    rd_Heating = BooleanField(verbose_name="Heating", default=False)
    rd_Lighting = BooleanField(verbose_name="Lighting", default=False)
    rd_Cooking = BooleanField(verbose_name="Cooking", default=False)
    rd_ApplianceUsage = BooleanField(verbose_name="Appliance usage", default=False)
    rd_SmartAppliances = BooleanField(
        verbose_name="Smart appliances & Smart metres", default=False
    )
    # DEMAND CHARACTERISTICS | COMMERCIAL DEMAND
    cd_Offices = BooleanField(verbose_name="Offices", default=False)
    cd_Warehouses = BooleanField(verbose_name="Warehouses", default=False)
    cd_Retail = BooleanField(verbose_name="Retail", default=False)
    # GRID MODEL
    gm_singleNode = BooleanField(verbose_name="Single-node model", default=False)
    gm_TranshipmentModel = BooleanField(
        verbose_name="Transhipment model", default=False
    )
    gm_LinearOptimal = BooleanField(
        verbose_name="Linear optimal power flow", default=False
    )
    # COST INCLUSION
    ci_FuelPrices = BooleanField(verbose_name="Fuel prices", default=False)
    ci_FuelHandling = BooleanField(verbose_name="Fuel handling", default=False)
    ci_Investment = BooleanField(verbose_name="Investment", default=False)
    ci_FixedOperation = BooleanField(
        verbose_name="Fixed Operation & Maintenance", default=False
    )
    ci_VariableOperation = BooleanField(
        verbose_name="Variable Operation & Maintenance", default=False
    )
    ci_CO2 = BooleanField(verbose_name="CO2 cost", default=False)
    # TIME STEPS
    ts_Minutely = BooleanField(verbose_name="Minutely", default=False)
    ts_Hourly = BooleanField(verbose_name="Hourly", default=False)
    ts_Monthly = BooleanField(verbose_name="Monthly", default=False)
    ts_Yearly = BooleanField(verbose_name="Yearly", default=False)
    ts_FiveYearly = BooleanField(verbose_name="Five-yearly", default=False)
    ts_other = CharField(verbose_name="Other", max_length=400, help_text="", null=True)
    # TIME HORIZON
    th_st = BooleanField(verbose_name="Short term (<= 5 years)", default=False)
    th_mt = BooleanField(verbose_name="medium term (>5-<15)", default=False)
    th_lt = BooleanField(verbose_name="long term (>=15)", default=False)
    th_other = CharField(verbose_name="Other", max_length=400, help_text="", null=True)

    fixed_units = BooleanField(
        verbose_name="Fixed units",
        help_text="Is the framework build on fixed base units?",
        default=False,
    )
    agricultural_demand = BooleanField(
        verbose_name="Agricultural demand",
        help_text="Which agricultural demands are already modelled with the framework?",  # noqa
        default=False,
    )
    new_components = BooleanField(
        verbose_name="New components",
        help_text="Is the framework build to allow for the implementation of new components?",  # noqa
        default=False,
    )
    variable_time_step = BooleanField(
        verbose_name="Variable time step",
        help_text="Is it possible to Model variable time steps with the framework?",  # noqa
        default=False,
    )
    variable_rolling_horizon = BooleanField(
        verbose_name="Variable rolling",
        help_text="Is it possible to Model a variable Rolling Horizon with the framework?",  # noqa
        default=False,
    )

    how_to_cite = CharField(
        verbose_name="Citation",
        help_text="How to cite the framework?",
        max_length=1000,
        null=True,
    )
    fw_appliance = CharField(
        verbose_name="Projects using the framework",
        help_text="Which research projects (on-going or past) apply the framework?",  # noqa
        max_length=1000,
        null=True,
    )
