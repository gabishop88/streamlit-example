import streamlit as st

def main():
    st.set_page_config(
        page_title="Farm Management App",
        page_icon="🌾",
        layout="wide"
    )

    st.title("Farm Management App")

    # User system
    st.markdown("---")
    st.write("👤 User System")

    # Define style for the boxes
    box_style = (
        "border-radius: 10px;"
        "padding: 20px;"
        "margin-bottom: 20px;"
        "background-color: #f0f0f0;"
    )

    # Data Inputs section
    st.markdown('<div style="{}">'.format(box_style), unsafe_allow_html=True)
    st.write("📝 Data Inputs")

    # Create a reactive empty container for Data Inputs section
    data_inputs_container = st.empty()

    # Data Visualization section
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('<div style="{}">'.format(box_style), unsafe_allow_html=True)
    st.write("📊 Data Visualization")

    # Create a reactive empty container for Data Visualization section
    data_viz_container = st.empty()

    # Dropdown menu for selecting content
    selected_content = st.selectbox("Select Content", ["Data Inputs", "Data Visualization"])

    # Update content based on dropdown selection
    if selected_content == "Data Inputs":
        data_inputs_container.write("Content for Data Inputs")
    elif selected_content == "Data Visualization":
        data_viz_container.write("Content for Data Visualization")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()


# import altair as alt
# import numpy as np
# import pandas as pd
# import streamlit as st

# """
# # Welcome to Streamlit!

# Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
# If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
# forums](https://discuss.streamlit.io).

# In the meantime, below is an example of what you can do with just a few lines of code:
# """

# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))
