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

    # Data Inputs section
    st.markdown("---")
    st.write("📝 Data Inputs")
    st.sidebar.title("Data Input Forms")
    data_input_form = st.sidebar.selectbox("Select Form", ["Field Manager", "Usage History", "Equipment List", "Field Testing Data", "Finances"])
    farm_name = st.selectbox("Farm Name", ["Farm 1", "Farm 2", "Farm 3"])
    st.write(f"Selected Farm: {farm_name}")
    st.sidebar.button("Upload Data")
    st.sidebar.button("Download Data")
    st.button("Filter")

    # Form
    st.subheader(data_input_form)
    st.write("Field Name: ")
    st.write("Field Group: (Optional)")
    st.write("Field Type: ")
    st.write("Boundaries: (Upload .shp files)")
    st.write("Certified Year: ")
    st.write("Active: ")
    if st.button("Add Row"):
        st.write("New Row Added")

    # Data Visualization section
    st.markdown("---")
    st.write("📊 Data Visualization")
    st.sidebar.title("Data Visualization Types")
    visualization_type = st.sidebar.selectbox("Select Visualization", ["Field Visualizer", "Crop Explorer", "Report Generator"])
    st.write(f"Selected Visualization: {visualization_type}")

    if visualization_type == "Field Visualizer":
        st.subheader("Field Visualizer Map")
        # Add interactive map component here

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
