from sqlalchemy import MetaData, Table, Column
from sqlalchemy import String, Numeric, ForeignKey


metadata = MetaData()


food_des = Table(
    'food_des', metadata,

    Column('NDB_No', String(5), primary_key=True),
    Column('FdGrp_Cd', String(4), ForeignKey('fd_group.FdGrp_Cd'),
           nullable=False),
    Column('Long_Desc', String(200), nullable=False),
    Column('Shrt_Desc', String(60), nullable=False),
    Column('ComName', String(100)),
    Column('ManufacName', String(65)),
    Column('Survey', String(1)),
    Column('Ref_desc', String(135)),
    Column('Refuse', Numeric(2)),
    Column('SciName', String(65)),
    Column('N_Factor', Numeric(4, 2)),
    Column('Pro_Factor', Numeric(4, 2)),
    Column('Fat_Factor', Numeric(4, 2)),
    Column('CHO_Factor', Numeric(4, 2)),
)


fd_group = Table(
    'fd_group', metadata,

    Column('FdGrp_Cd', String(4), primary_key=True),
    Column('FdGrp_Desc', String(60), nullable=False),
)


langual = Table(
    'langual', metadata,

    Column('NDB_No', String(5), ForeignKey('food_des.NDB_No'),
           primary_key=True),
    Column('Factor_Code', String(5), ForeignKey('langdesc.Factor_Code'),
           primary_key=True),
)


langdesc = Table(
    'langdesc', metadata,

    Column('Factor_Code', String(5), primary_key=True),
    Column('Description', String(140), nullable=False),
)


nut_data = Table(
    'nut_data', metadata,

    Column('NDB_No', String(5), ForeignKey('food_des.NDB_No'),
           primary_key=True),
    Column('Nutr_No', String(3), ForeignKey('nutr_def.Nutr_No'),
           primary_key=True),
    Column('Nutr_Val', Numeric(10, 3), nullable=False),
    Column('Num_Data_Pts', Numeric(5), nullable=False),
    Column('Std_Error', Numeric(8, 3)),
    Column('Src_Cd', String(2), ForeignKey('src_cd.Src_Cd'),
           nullable=False),
    Column('Deriv_Cd', String(4), ForeignKey('deriv_cd.Deriv_Cd')),
    Column('Ref_NDB_No', String(5), ForeignKey('food_des.NDB_No')),
    Column('Add_Nutr_Mark', String(1)),
    Column('Num_Studies', Numeric(2)),
    Column('Min', Numeric(10, 3)),
    Column('Max', Numeric(10, 3)),
    Column('DF', Numeric(4)),
    Column('Low_EB', Numeric(10, 3)),
    Column('Up_EB', Numeric(10, 3)),
    Column('Stat_cmt', String(10)),
    Column('AddMod_Date', String(10)),
    Column('CC', String(1)),
)


nutr_def = Table(
    'nutr_def', metadata,

    Column('Nutr_No', String(3), primary_key=True),
    Column('Units', String(7), nullable=False),
    Column('Tagname', String(20)),
    Column('NutrDesc', String(60), nullable=False),
    Column('Num_Dec', String(1), nullable=False),
    Column('SR_Order', Numeric(6), nullable=False),
)


src_cd = Table(
    'src_cd', metadata,

    Column('Src_Cd', String(2), primary_key=True),
    Column('SrcCd_Desc', String(60), nullable=False),
)


deriv_cd = Table(
    'deriv_cd', metadata,

    Column('Deriv_Cd', String(4), primary_key=True),
    Column('Deriv_Desc', String(120), nullable=False),
)


weight = Table(
    'weight', metadata,

    Column('NDB_No', String(5), ForeignKey('food_des.NDB_No'),
           primary_key=True),
    Column('Seq', String(2), primary_key=True),
    Column('Amount', Numeric(5, 3), nullable=False),
    Column('Msre_Desc', String(84), nullable=False),
    Column('Gm_Wgt', Numeric(7, 1), nullable=False),
    Column('Num_Data_Pts', Numeric(3)),
    Column('Std_Dev', Numeric(7, 3)),
)


footnote = Table(
    'footnote', metadata,

    Column('NDB_No', String(5), ForeignKey('food_des.NDB_No'),
           nullable=False),
    Column('Footnt_No', String(4), nullable=False),
    Column('Footnt_Typ', String(1), nullable=False),
    Column('Nutr_No', String(3)),
    Column('Footnt_Txt', String(200), nullable=False),
)


datsrcln = Table(
    'datsrcln', metadata,

    Column('NDB_No', String(5), ForeignKey('food_des.NDB_No'),
           primary_key=True),
    Column('Nutr_No', String(3), ForeignKey('nutr_def.Nutr_No'),
           primary_key=True),
    Column('DataSrc_ID', String(6), ForeignKey('data_src.DataSrc_ID'),
           primary_key=True),
)


data_src = Table(
    'data_src', metadata,

    Column('DataSrc_ID', String(6), primary_key=True),
    Column('Authors', String(255)),
    Column('Title', String(255), nullable=False),
    Column('Year', String(4)),
    Column('Journal', String(135)),
    Column('Vol_City', String(16)),
    Column('Issue_State', String(5)),
    Column('Start_Page', String(5)),
    Column('End_Page', String(5)),
)
