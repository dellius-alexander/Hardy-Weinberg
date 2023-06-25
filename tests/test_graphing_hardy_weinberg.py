from mpl_toolkits.mplot3d.proj3d import proj_transform
from matplotlib.text import Annotation
from . import HardyWeinberg, HardyWeinbergStats, Gene, get_logger, generate_population
import matplotlib.pyplot as plt

log = get_logger(__name__)

plt.style.use("ggplot")


class Annotation3D(Annotation):
    '''Annotate the point xyz with text s'''

    def __init__(self, s, xyz, *args, **kwargs):
        Annotation.__init__(self,s, xy=(0,0), *args, **kwargs)
        self._verts3d = xyz if xyz else kwargs.get('xyz', None)

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.xy=(xs,ys)
        Annotation.draw(self, renderer)

def annotate3D(ax, s, *args, **kwargs):
    '''add anotation text s to to Axes3d ax'''

    tag = Annotation3D(s, *args, **kwargs)
    ax.add_artist(tag)


# --------------------------------------------------------------------------- #
def test_plotting_hws():
    population = generate_population(10000)
    log.info(f"\nPopulation: {len(population)}")
    res: HardyWeinberg = HardyWeinberg(genes=population)
    log.info(f"Result: {res.stats.data_structure}")
    log.info(f"Chi-Squared: {res.stats.chi_square_test}")
    data = res.stats.data_structure
    log.info(f"Population Data: \n{data[0:][0][0][0]}")
    log.info(f"Expected Data: \n{data[1:][0][0][0]}")
    log.info(f"Allele Frequency Data: \n{data[2:][0][0][0]}")
    # 3d scatter plot stats and figures
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.scatter3D(
        xs=data[0:][0][0][0],
        ys=data[2:][0][0][0] * 100,
        zs=data[1:][0][0][0],
        c="g",
        marker="v",
        zdir="z",
        depthshade=True,
        label="Hd"
    )
    ax.scatter3D(
        xs=data[0:][0][0][1],
        ys=data[2:][0][0][1] * 100,
        zs=data[1:][0][0][1],
        c="r",
        marker="^",
        zdir="z",
        depthshade=True,
        label="Hr"
    )
    ax.scatter3D(
        xs=data[0:][0][0][2],
        ys=data[2:][0][0][2] * 100,
        zs=data[1:][0][0][2],
        c="b",
        marker="o",
        zdir="z",
        depthshade=True,
        label="He"
    )

    ax.plot3D(
        xs=data[0:][0][0],
        ys=[a * 100 for a in data[2:][0][0]],
        zs=data[1:][0][0],
    )

    ax.legend(["Homo-Dominant", "Homo-Recessive", "Heterozygous"], loc='upper left')

    plt.xlabel("Population (x)")
    plt.ylabel("Allele Frequency (y)")
    ax.set_zlabel("Expected (z)")
    # Rotate the axes and update
    angle = 45
    # Normalize the angle to the range [-180, 180] for display
    angle_norm = (angle + 180) % 360 - 180
    elev = angle_norm
    azim = 0
    roll = 0
    # Update the axis view and title
    ax.view_init(elev, azim, roll)
    plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))
    # plt.draw()
    # plt.pause(0.01)


if __name__ == "__main__":
    test_plotting_hws()

