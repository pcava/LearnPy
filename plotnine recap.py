# Plotnine Recap
# see also:
# https://plotnine.readthedocs.io/en/stable/

from plotnine import (
    ggplot, aes, geom_col, facet_wrap, 
    coord_flip, theme, theme_dark, theme_minimal
)

# ex_01

# convert 'Bikeshop Name' to a categorical to sort the chart
bikeshop_order = bikeshop_revenue_long_df \
    .groupby('Bikeshop Name') \
    .sum() \
    .sort_values('Revenue') \
    .index \
    .tolist()
bikeshop_revenue_long_df['Bikeshop Name'] = pd.Categorical(bikeshop_revenue_long_df['Bikeshop Name'], categories=bikeshop_order)

# and make the barchart
ggplot(
    mapping = aes(x='Bikeshop Name', y='Revenue', fill='Category 1'),
    data = bikeshop_revenue_long_df
) \
    + geom_col() \
    + coord_flip() \
    + facet_wrap('Category 1') \
    + theme_minimal() \
    + theme(legend_position = 'none')


# ex_02

ggplot(
  mapping = aes(x='order_date', y='total_price'), 
  data = sales_by_month_cat_2
  ) + \
  geom_line(color='#2c3e50') + \
  geom_smooth(method = 'lm', se=False, color='blue') + \
  facet_wrap(
    facets='category_2',
    ncol=3,
    scales="free_y"
  ) + \
  scale_y_continuous(
    labels = currency_format(prefix="$", digits=0, big_mark="'")
  ) + \
  scale_x_datetime(
    breaks = date_breaks('2 years'),
    labels = date_format(fmt="%Y-%m")
  ) + \
  labs(
    title = "Revenue by Week",
    x = "",
    y = "Revenue"
  ) + \
  theme_minimal() + \
  theme(
    subplots_adjust={'wspace': 0.35},
    axis_text_y=element_text(size=6),
    axis_text_x=element_text(size=6)
  )
  
  
  
# ex_03

g = ( 
    # Canvas 
    ggplot( 
        mapping = aes(x='order_date', y='total_price'), 
        data    = bike_sale_y_df 
    ) 
     
    # Geometries 
    + geom_col(fill = '#2C3E50') 
    + geom_smooth( 
        method  = 'lm', 
        se      = False, 
        color   = 'dodgerblue') 
     
    # Formatting 
    + expand_limits(y=[0,20e6]) 
    + scale_y_continuous(labels = dollar_format(digits=0, big_mark="'")) 
    + scale_x_datetime( 
        date_labels = "%Y", 
        date_breaks = "2 years" 
    ) 
     
    + labs( 
        title = 'Revenue by Year', 
        x = '', 
        y = 'Revenue' 
    ) 
     
    + theme_minimal() 
) 

g

# Saving a plot ---- 
g.save("07_visualization/bike_sales_y.jpg") 
# What is a plotnine plot? ---- 
type(g) # plotnine.ggplot.ggplot 
g.data # underlying data frame 



# scatter plot
(
    ggplot(
        mapping=aes(x='quantity', y='total_price'),
        data = quantity_total_price_by_order_df
    )
    + geom_point(alpha = .5)
    + geom_smooth(method = 'lm')
)


# line plot
(
    ggplot(
        mapping = aes(x='order_date', y='total_price'),
        data = bikes_sales_m_df
    )
    + geom_line()
    + geom_smooth(method = 'lm', se = False)
    + geom_smooth(
        method = 'loess',
        se = False, 
        span = .2,
        color = 'dodgerblue')
)


# bar chart
# convert category_2 to a category data type if you need a sorted bat chart
bike_sales_cat2_order_df = df \
    .groupby('category_2') \
    .agg({'total_price': np.sum}) \
    .sort_values('total_price', ascending=True) \
    .index \
    .to_list()
    
from plydata.cat_tools import cat_reorder
bike_sales_cat2_df = df \
    .groupby('category_2') \
    .agg({'total_price': np.sum}) \
    .reset_index() \
    .assign(
        category_2 = 
            # lambda x: pd.Categorical(x['category_2'], 
            # categories=bike_sales_cat2_order_df)
            lambda x: cat_reorder(x['category_2'], x['total_price'], ascending = True)
    )

(
    ggplot(
        mapping=aes(x='category_2', y='total_price'),
        data= bike_sales_cat2_df
    )
    + geom_col(fill = "#2c3e50")
    + coord_flip()
    + theme_minimal()
)


# Histograms
g_hist_p9 = (
    ggplot(
        mapping=aes(x='price', fill='frame_material'),
        data=unit_price_by_frame_df
    ) 
    + geom_histogram(bins = 25, color = 'white')
)
g_hist_p9 + facet_grid(facets=['frame_material','.'])


# Density plots
g_dens_p9 = (
    ggplot(
        mapping=aes(x='price', fill='frame_material'),
        data=unit_price_by_frame_df
    ) 
    + geom_density(alpha = .5)
)
g_dens_p9 + facet_wrap("frame_material", ncol=1)


# Box plots
(
    ggplot(
        mapping=aes('category_2','price'),
        data = df
        )
    + geom_boxplot()
    + coord_flip()
)

# using Plotnine's internal function 'reorder' without converting category_2 to Categorical
# https://stackoverflow.com/questions/62507299/plotting-in-sorted-order-using-plotnine
(
    ggplot(
        mapping=aes('reorder(category_2,price)','price'),
        data = df
        )
    + geom_boxplot()
    + coord_flip()
)


# Violin plots
(
    ggplot(
        mapping=aes('category_2','price'),
        data = unit_price_by_cat2_df
        )
    + geom_violin()
    + geom_jitter(width=.15, alpha=.5)
    + coord_flip()
)


# Text and Labels (similar to Text but with an additional background)
(
    ggplot(aes('order_date', 'total_price'), bike_sales_y_df)
    + geom_col(fill = '#2c3e50')
    + geom_smooth(method='lm', se=False, color='dodgerblue')
    + geom_text(
        aes(
            label   = 'total_price_text'),
            va      = 'top',
            size    = 8,
            nudge_y = -1.2e5,
            color   = 'white'
    )
    + geom_label(
        label = "Major Demand",
        color = 'red',
        nudge_y = 1e6,
        size = 10,
        # data masking
        data = bike_sales_y_df[
            bike_sales_y_df['order_date'].dt.year == 2013
        ]
    )
    + expand_limits(y=[0, 20e6])
    + scale_x_datetime(date_labels = '%Y')
    + scale_y_continuous(labels = usd)
    + theme_minimal()
)


# Plot Customizations: Facets, Scales, Themes, and Labs
# - Facets: Used for visualizing groups with subplots
# - Scales: Used for transforming x/y axis and colors/fills
# - Theme: Used to adjust attributes of the plot
# - Labs: Used to adjust title, x/y axis labels

matplotlib.pyplot.style.available 
# matplotlib.pyplot.style.use('dark_background') 
# matplotlib.pyplot.style.use('default')

g = ( 
    ggplot(aes('order_date','total_price'), bike_sales_cat2_m_df) 
    + geom_line(color='#2C3E50') 
    + geom_smooth(span=.2, se=False, color = 'dodgerblue') 
    + facet_wrap(facets = 'category_2', ncol=3, scales='free_y') 
    + scale_x_datetime(date_labels = '%Y', date_breaks = '2 years') 
    + scale_y_continuous(labels=usd) 
    + scale_color_cmap_d() 
    + theme_minimal() 
    + theme( 
        strip_text=element_text(color='white'),  
        strip_background=element_rect(fill='#2C3E50'), 
        legend_position='none', 
        figure_size= (16, 8), 
        subplots_adjust= {'wspace': .25} 
    ) 
    + labs( 
        title = 'Revenue by Month and Category 2', 
        x = 'Date', 
        y = 'Revenue' 
    ) 
) 

g.save("07_visualization/bike_sales_cat2_m.jpg")


